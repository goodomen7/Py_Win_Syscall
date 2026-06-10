# py-windows-syscall-bench

**English** | [中文](README.zh.md)

A benchmark for evaluating **LLM chain-of-thought (CoT) reasoning** that links a
single Python source line to the **Windows native system call** it triggers, and
judges the reasoning against curated ground truth.

Each task gives a model a Python program, a highlighted *target line*, and the
captured syscall trace, and asks the model to explain which line produces a given
syscall and why. Model answers are then scored node-by-node by a judge model.

## Statistics

| Metric | Count |
| --- | --- |
| Standard-library modules | 9 |
| Tasks | 113 |
| Tasks with curated best answer + judge scores | 105 |
| Models evaluated | 11 |

**Modules:** `mmap`, `msvcrt`, `multiprocessing`, `os`, `signal`, `socket`,
`ssl`, `time`, `uuid`

**Models evaluated:** ERNIE-3.5-8K, claude-opus-4-7, claude-sonnet-4-6,
deepseek-v3.2, doubao-seed-2-0-lite-260215, gemini-2.5-pro,
gemini-3-pro-preview-thinking, glm-4, gpt-5.2, gpt-5.5, grok-4-20-reasoning

(See [`metadata.json`](metadata.json) for the authoritative list and per-module
counts in each [`data/<module>/metadata.json`](data).)

## Layout

```
py-windows-syscall-bench/
├── README.md
├── metadata.json                  # global stats, module list, model list, schema notes
├── reorganize.py                  # script that builds this tree from the raw data
└── data/
    └── <module>/                  # one folder per Python stdlib module under test
        ├── module_under_test.py   # aggregate program exercising the module's functions
        ├── metadata.json          # per-module task list and counts
        └── tasks/
            └── <module>-NN/       # one self-contained task (e.g. socket-07)
                ├── task.json          # task metadata (target line, target syscall, flags)
                ├── input/             # exactly what is shown to the model under test
                │   ├── context.py        #   the program containing the target line
                │   ├── target_line.txt   #   the highlighted line to reason about
                │   └── trace.txt         #   captured syscall trace
                ├── ground_truth/
                │   ├── candidates.jsonl  # all curated candidate answers (one JSON/line)
                │   ├── best.json         # the selected best answer*
                │   └── selection.json    # judge rationale for the selection*
                ├── predictions.jsonl  # answers under test, one JSON line per model
                ├── scores.jsonl       # judge scores, one JSON line per model*
                └── raw/               # provenance / generation artifacts
                    ├── source.py         # instrumented script that produced the trace
                    └── trace.txt         # raw, full syscall trace
```

\* `best.json`, `selection.json`, and `scores.jsonl` are present for the 105
fully-processed tasks. The remaining 8 tasks ship with inputs, candidate answers,
and model predictions only. Each task's `task.json` records `has_best_answer` and
`has_scores` so consumers can filter.

## File formats

### `task.json`
```json
{
  "task_id": "mmap-01",
  "library": "mmap",
  "target_line": "m_anon = mmap.mmap(-1, 4096)",
  "target_syscall": "NtCreateSection",
  "num_models_answered": 11,
  "num_models_scored": 11,
  "has_best_answer": true,
  "has_scores": true
}
```

### `ground_truth/best.json` (and each line of `candidates.jsonl`)
The expected CoT answer, structured as facts (`F1`–`F3`) and logic (`L1`–`L3`):
```json
{
  "conclusion": "代码行[m_anon = mmap.mmap(-1, 4096)]最可能触发或产生该系统调用",
  "facts": {
    "F1": {"syscall": "NtCreateSection", "summary": "创建内存区段用于映射"},
    "F2": {"option": "B", "reason": "匿名映射创建内存区段"},
    "F3": "创建区段对象"
  },
  "logic": {
    "L1": "mmap.mmap(-1, 4096) → Python mmap 模块创建匿名映射 → NtCreateSection",
    "L2": {"option": "A", "reason": "创建匿名mmap需创建section对象"},
    "L3": {"option": "A", "reason": "调用mmap构造即会立即创建映射"}
  }
}
```

### `predictions.jsonl` (one line per model)
```json
{"model": "claude-opus-4-7", "ok": true, "latency_s": 6.76, "error": null, "raw": "{...model answer JSON as a string...}"}
```

### `scores.jsonl` (one line per model)
Per-node `Correct`/`Incorrect` judgements with evidence, over the seven nodes
`Conclusion`, `F1`, `F2`, `F3`, `L1`, `L2`, `L3`:
```json
{"sample_id": "sample01", "target_model": "grok-4-20-reasoning",
 "final": {"final_node_scores": {"Conclusion": "Incorrect", "F1": "Incorrect", "F2": "Correct", "...": "..."},
           "final_evidence": {"...": {"model_quote": ["..."], "gt_clause_hit": ["..."], "reason": "..."}}}}
```

## Reproducing the layout

`reorganize.py` is the deterministic transform from the original raw data
(per-module `func_scripts/`, `traces/`, `mk_gt/`, `gt/`, `ques_result/`,
`score_result/` folders) into this `data/` tree. It is included for provenance.

## Notes

- Reasoning text in the ground truth and judge output is in Chinese; the schema
  keys are in English.
- Traces were captured on Windows (Python 3.13) via ETW; native syscalls use the
  `Nt*` naming convention.
