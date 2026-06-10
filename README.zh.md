# py-windows-syscall-bench

[English](README.md) | **中文**

一个用于评测**大模型思维链(CoT)推理能力**的 benchmark:给定一段 Python 代码,
判断其中某一行源代码触发了哪个 **Windows 原生系统调用(syscall)**,并对推理过程
进行结构化打分。

每个任务向被测模型提供一段 Python 程序、一行高亮的*目标代码行*以及捕获到的系统调用
trace,要求模型解释"哪一行代码产生了某个系统调用、为什么"。模型的回答随后由评测模型
逐节点(node-by-node)打分。

## 数据统计

| 指标 | 数量 |
| --- | --- |
| 标准库模块 | 9 |
| 任务数 | 113 |
| 含标准答案 + 评分的任务 | 105 |
| 参与评测的模型 | 11 |

**模块:** `mmap`、`msvcrt`、`multiprocessing`、`os`、`signal`、`socket`、
`ssl`、`time`、`uuid`

**参评模型:** ERNIE-3.5-8K、claude-opus-4-7、claude-sonnet-4-6、
deepseek-v3.2、doubao-seed-2-0-lite-260215、gemini-2.5-pro、
gemini-3-pro-preview-thinking、glm-4、gpt-5.2、gpt-5.5、grok-4-20-reasoning

(权威列表见 [`metadata.json`](metadata.json),各模块的任务数见
[`data/<模块>/metadata.json`](data)。)

## 目录结构

```
py-windows-syscall-bench/
├── README.md                      # 英文说明
├── README.zh.md                   # 本文件(中文说明)
├── metadata.json                  # 全局统计、模块列表、模型列表、格式说明
├── reorganize.py                  # 由原始数据生成本结构的脚本
└── data/
    └── <模块>/                    # 每个被测 Python 标准库一个文件夹
        ├── module_under_test.py   # 汇总该模块所有参测函数的程序
        ├── metadata.json          # 该模块的任务列表与计数
        └── tasks/
            └── <模块>-NN/         # 一个自包含的任务(例:socket-07)
                ├── task.json          # 任务元数据(目标行、目标系统调用、标记位)
                ├── input/             # 完全等同于展示给被测模型的输入
                │   ├── context.py        #   包含目标行的程序
                │   ├── target_line.txt   #   需要推理的高亮代码行
                │   └── trace.txt         #   捕获到的系统调用 trace
                ├── ground_truth/
                │   ├── candidates.jsonl  # 所有候选标准答案(每行一个 JSON)
                │   ├── best.json         # 被选定的最佳答案*
                │   └── selection.json    # 评测模型给出的选择理由*
                ├── predictions.jsonl  # 被测模型的回答,每行一个模型
                ├── scores.jsonl       # 评测打分,每行一个模型*
                └── raw/               # 溯源 / 生成产物
                    ├── source.py         # 产生该 trace 的(带插桩)脚本
                    └── trace.txt         # 原始、完整的系统调用 trace
```

\* `best.json`、`selection.json`、`scores.jsonl` 仅在 105 个完整处理的任务中存在。
其余 8 个任务只提供输入、候选答案与模型回答。每个任务的 `task.json` 都记录了
`has_best_answer` 和 `has_scores` 标记,便于使用者过滤筛选。

## 文件格式

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

### `ground_truth/best.json`(以及 `candidates.jsonl` 中的每一行)
期望的思维链答案,由事实节点(`F1`–`F3`)与逻辑节点(`L1`–`L3`)构成:
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

### `predictions.jsonl`(每行一个模型)
```json
{"model": "claude-opus-4-7", "ok": true, "latency_s": 6.76, "error": null, "raw": "{...模型答案 JSON(以字符串形式)...}"}
```

### `scores.jsonl`(每行一个模型)
对 `Conclusion`、`F1`、`F2`、`F3`、`L1`、`L2`、`L3` 七个节点逐一给出
`Correct`/`Incorrect` 判定及证据:
```json
{"sample_id": "sample01", "target_model": "grok-4-20-reasoning",
 "final": {"final_node_scores": {"Conclusion": "Incorrect", "F1": "Incorrect", "F2": "Correct", "...": "..."},
           "final_evidence": {"...": {"model_quote": ["..."], "gt_clause_hit": ["..."], "reason": "..."}}}}
```

## 复现该结构

`reorganize.py` 是从原始数据(各模块下的 `func_scripts/`、`traces/`、`mk_gt/`、
`gt/`、`ques_result/`、`score_result/` 文件夹)到当前 `data/` 结构的确定性转换脚本,
随仓库附带以供溯源。

## 备注

- 标准答案与评测输出中的推理文本为中文;结构字段(schema key)为英文。
- trace 在 Windows(Python 3.13)上通过 ETW 捕获,原生系统调用采用 `Nt*` 命名约定。
