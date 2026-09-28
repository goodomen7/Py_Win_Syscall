# py-windows-syscall-bench

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
| Tasks with curated best answer + judge scores | 113 |
| Models evaluated | 14 |

**Modules:** `mmap`, `msvcrt`, `multiprocessing`, `os`, `signal`, `socket`,
`ssl`, `time`, `uuid`

**Models evaluated:** claude-opus-4-7, claude-opus-4.6, deepseek-v3.2,
gemini-2.5-pro, gemini-3.1-pro-preview, gemini-3.1-pro-preview-thinking,
glm-5, gpt-5-codex, gpt-5.2, gpt-5.5, llama-3.3-70b-instruct,
qwen3-coder-30b-a3b-instruct, qwen3.5-27b, qwen3.6-27b

(See [`metadata.json`](metadata.json) for the authoritative list and per-module
counts in each [`data/<module>/metadata.json`](data).)

## Layout

```
py-windows-syscall-bench/
├── README.md
├── metadata.json                  # global stats, module list, model list, schema notes
├── reorganize.py                  # script that builds this tree from the raw data
├── reference/                     # static stdlib-function → NtAPI truth map (ground-truth source)
│   ├── ground_truth.jsonl         #   one record per function (primary form)
│   ├── ground_truth.json          #   same, grouped by library
│   ├── ground_truth.csv           #   flattened (function, syscall) pairs
│   ├── schema.json                #   JSON Schema for a record
│   ├── build_reference.py         #   builder: source_md/*.md → the artifacts
│   └── source_md/                 #   original research notes (full call chains)
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

\* `best.json`, `selection.json`, and `scores.jsonl` are present for all 113
tasks in this release. Each task's `task.json` records `has_best_answer` and
`has_scores` so consumers can filter.

## Reproducing the layout

`reorganize.py` is the deterministic transform from the original raw data
(per-module `func_scripts/`, `traces/`, `mk_gt/`, `gt/`, `ques_result/`,
`score_result/` folders) into this `data/` tree. It is included for provenance.

## Notes

- Reasoning text in the ground truth and judge output is in Chinese; the schema
  keys are in English.
- Traces were captured on Windows (Python 3.13) via ETW; native syscalls use the
  `Nt*` naming convention.
