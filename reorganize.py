#!/usr/bin/env python3
"""Reorganize the raw py_windows_syscall data into a clean benchmark layout.

Source layout (per library <lib>):
    <lib>/example.py                         aggregate module-under-test
    <lib>/func_scripts/func_NN.py            instrumented script that triggers syscalls
    <lib>/traces/func_NN_syscall.txt         raw ETW/syscall trace
    <lib>/mk_gt/sampleNN/{target_line.txt, example.py, syscall.txt}   model input bundle
    <lib>/gt/sampleNN/{results.jsonl, result_best.json, select_reason.json}
    <lib>/ques_result/sampleNN/results.jsonl model answers (one JSON line per model)
    <lib>/score_result/sampleNN/eval_report.jsonl  judge scores (one line per model)

Target layout:
    data/<lib>/
        module_under_test.py
        metadata.json
        tasks/<lib>-NN/
            input/{context.py, target_line.txt, trace.txt}
            ground_truth/{candidates.jsonl, best.json, selection.json}
            predictions.jsonl
            scores.jsonl                     (only if it exists upstream)
            raw/{source.py, trace.txt}
            task.json
    metadata.json                            global stats
"""
import json
import re
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent
OUT = SRC.parent / "py-windows-syscall-bench"

LIBRARIES = ["mmap", "msvcrt", "multiprocessing", "os", "signal",
             "socket", "ssl", "time", "uuid"]


def sample_num(name: str) -> str:
    m = re.search(r"(\d+)", name)
    return m.group(1) if m else name


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def jsonl_models(path: Path, key: str):
    models = []
    if not path.exists():
        return models
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            models.append(json.loads(line).get(key))
        except Exception:
            pass
    return [m for m in models if m]


def copy_if(src: Path, dst: Path):
    if src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        return True
    return False


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    global_stats = {
        "name": "py-windows-syscall-bench",
        "version": "1.0.0",
        "description": ("Benchmark for evaluating LLM chain-of-thought reasoning that "
                        "links a Python source line to the Windows native syscall it "
                        "triggers, judged against curated ground truth."),
        "task_format": {
            "input": "Curated prompt unit: target code line, surrounding context, and syscall trace.",
            "ground_truth": "Best curated answer plus all candidate answers and the selection rationale.",
            "prediction": "One JSON line per evaluated model with its raw answer.",
            "score": "Per-node (Conclusion/F1/F2/F3/L1/L2/L3) Correct/Incorrect judgement per model.",
        },
        "libraries": [],
        "models_evaluated": set(),
        "totals": {"libraries": 0, "tasks": 0, "scored_tasks": 0,
                   "tasks_with_best_answer": 0},
    }

    for lib in LIBRARIES:
        lib_src = SRC / lib
        if not lib_src.is_dir():
            continue
        lib_out = OUT / "data" / lib
        tasks_out = lib_out / "tasks"
        tasks_out.mkdir(parents=True, exist_ok=True)

        copy_if(lib_src / "example.py", lib_out / "module_under_test.py")

        sample_dirs = sorted(
            [p for p in (lib_src / "mk_gt").iterdir() if p.is_dir()],
            key=lambda p: int(sample_num(p.name)),
        )

        lib_tasks = []
        for sdir in sample_dirs:
            num = sample_num(sdir.name)
            nn = num.zfill(2)
            task_id = f"{lib}-{nn}"
            t_out = tasks_out / task_id

            # input bundle
            copy_if(sdir / "example.py", t_out / "input" / "context.py")
            copy_if(sdir / "target_line.txt", t_out / "input" / "target_line.txt")
            copy_if(sdir / "syscall.txt", t_out / "input" / "trace.txt")

            # ground truth
            gt = lib_src / "gt" / sdir.name
            copy_if(gt / "results.jsonl", t_out / "ground_truth" / "candidates.jsonl")
            has_best = copy_if(gt / "result_best.json", t_out / "ground_truth" / "best.json")
            copy_if(gt / "select_reason.json", t_out / "ground_truth" / "selection.json")

            # predictions
            pred = lib_src / "ques_result" / sdir.name / "results.jsonl"
            has_pred = copy_if(pred, t_out / "predictions.jsonl")

            # scores
            score = lib_src / "score_result" / sdir.name / "eval_report.jsonl"
            has_score = copy_if(score, t_out / "scores.jsonl")

            # raw artifacts
            copy_if(lib_src / "func_scripts" / f"func_{nn}.py", t_out / "raw" / "source.py")
            copy_if(lib_src / "traces" / f"func_{nn}_syscall.txt", t_out / "raw" / "trace.txt")

            # per-task metadata
            target_line = ""
            tl = sdir / "target_line.txt"
            if tl.exists():
                target_line = tl.read_text(encoding="utf-8").strip()
            best = read_json(gt / "result_best.json") or {}
            syscall = (best.get("facts", {}) or {}).get("F1", {})
            syscall = syscall.get("syscall") if isinstance(syscall, dict) else None

            models = jsonl_models(pred, "model")
            scored_models = jsonl_models(score, "target_model")
            global_stats["models_evaluated"].update(models)
            global_stats["models_evaluated"].update(scored_models)

            task_meta = {
                "task_id": task_id,
                "library": lib,
                "target_line": target_line,
                "target_syscall": syscall,
                "num_models_answered": len(models),
                "num_models_scored": len(scored_models),
                "has_best_answer": has_best,
                "has_scores": has_score,
            }
            (t_out / "task.json").write_text(
                json.dumps(task_meta, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            lib_tasks.append(task_meta)
            global_stats["totals"]["tasks"] += 1
            if has_score:
                global_stats["totals"]["scored_tasks"] += 1
            if has_best:
                global_stats["totals"]["tasks_with_best_answer"] += 1

        lib_meta = {
            "library": lib,
            "num_tasks": len(lib_tasks),
            "num_scored_tasks": sum(1 for t in lib_tasks if t["has_scores"]),
            "num_tasks_with_best_answer": sum(1 for t in lib_tasks if t["has_best_answer"]),
            "tasks": [t["task_id"] for t in lib_tasks],
        }
        (lib_out / "metadata.json").write_text(
            json.dumps(lib_meta, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        global_stats["libraries"].append(lib)
        global_stats["totals"]["libraries"] += 1

    global_stats["models_evaluated"] = sorted(global_stats["models_evaluated"])
    (OUT / "metadata.json").write_text(
        json.dumps(global_stats, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print("Done. Wrote benchmark to", OUT)
    print(json.dumps(global_stats["totals"], indent=2))


if __name__ == "__main__":
    main()
