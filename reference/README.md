# reference/ — static stdlib-function → Windows NtAPI truth map

**English** | [中文](#中文说明)

This directory holds the **ground-truth source** for the benchmark: a static,
hand-curated mapping from a Python standard-library function to the set of
Windows native system calls (`Nt*`) it can theoretically reach. It answers the
question *"which NtAPIs should a given line of Python touch?"* independently of
any model output, and is the reference the per-task ground truth in
[`../data/`](../data) is expected to be consistent with.

It is broader than the evaluation set: it currently covers **12 modules**
(adding `select`, `winreg`, `winsound`) versus the 9 scored in `data/`.

## Files

| File | Purpose |
| --- | --- |
| `ground_truth.jsonl` | **Primary** machine-readable form — one JSON record per function. |
| `ground_truth.json` | Same data grouped by library, for browsing/diffing. |
| `ground_truth.csv` | Flattened `(function, syscall)` pairs, for spreadsheets. |
| `schema.json` | JSON Schema (draft-07) for one `ground_truth.jsonl` record. |
| `build_reference.py` | Deterministic builder: `source_md/*.md` → the three artifacts. |
| `source_md/` | Original research notes (full call chains) kept for provenance. |

## Record format (`ground_truth.jsonl`)

```json
{
  "id": "os-02",
  "library": "os",
  "function": "os.chdir",
  "syscalls": [
    {"name": "NtOpenFile", "condition": null},
    {"name": "NtQueryVolumeInformationFile", "condition": null},
    {"name": "NtClose", "condition": null}
  ],
  "source": "系统调用统计_windows_os库.md"
}
```

- `syscalls[].condition` is free-text (Chinese) describing when that syscall
  fires; `null` means unconditional. A function may list the same syscall under
  different conditions.
- Syscall names use the `Nt*` native convention, matching the traces in
  `data/`.

## Rebuilding

The artifacts are generated, not edited by hand. To change the mapping, edit the
relevant note in `source_md/` (its `## 总结` summary table) and rerun:

```bash
python3 reference/build_reference.py
```

## Stats

12 modules · 131 functions · 208 (function, syscall) pairs.

| module | functions | | module | functions |
| --- | --- | --- | --- | --- |
| `os` | 36 | | `time` | 12 |
| `socket` | 43 | | `winreg` | 14 |
| `ssl` | 5 | | `uuid` | 5 |
| `mmap` | 4 | | `msvcrt` | 3 |
| `signal` | 3 | | `winsound` | 3 |
| `multiprocessing` | 2 | | `select` | 1 |

---

## 中文说明

[English](#reference--static-stdlib-function--windows-ntapi-truth-map) | **中文**

本目录是整个 benchmark 的 **ground truth 来源**:一张静态、人工整理的映射表,记录每个
Python 标准库函数在理论上会触达的 Windows 原生系统调用(`Nt*`)。它回答的是
*“某一行 Python 代码理论上应该触发哪些 NtAPI”*,独立于任何模型输出,是
[`../data/`](../data) 中各任务级 ground truth 需要保持一致的参照基准。

它比评测集覆盖更广:目前包含 **12 个模块**(额外加入 `select`、`winreg`、`winsound`),
而 `data/` 中实际判分的是 9 个。

### 文件说明

| 文件 | 用途 |
| --- | --- |
| `ground_truth.jsonl` | **主格式** —— 机器可读,每行一条函数记录。 |
| `ground_truth.json` | 同样数据,按库分组,便于浏览 / diff。 |
| `ground_truth.csv` | 拍平的 `(函数, 系统调用)` 对,便于用表格软件查看。 |
| `schema.json` | 单条 `ground_truth.jsonl` 记录的 JSON Schema(draft-07)。 |
| `build_reference.py` | 确定性构建脚本:`source_md/*.md` → 上述三个产物。 |
| `source_md/` | 原始调研笔记(含完整调用链),保留用于溯源。 |

### 记录格式(`ground_truth.jsonl`)

```json
{
  "id": "os-02",
  "library": "os",
  "function": "os.chdir",
  "syscalls": [
    {"name": "NtOpenFile", "condition": null},
    {"name": "NtQueryVolumeInformationFile", "condition": null},
    {"name": "NtClose", "condition": null}
  ],
  "source": "系统调用统计_windows_os库.md"
}
```

- `syscalls[].condition` 为自由文本(中文),描述该系统调用在何种条件下触发;
  `null` 表示无条件触发。同一函数可在不同条件下列出相同的系统调用。
- `syscalls[].arg` 为可选字段,记录限定该系统调用的信息类 / 控制参数,
  例如 `NtQueryInformationProcess` 的 `ProcessTimes`。
- 系统调用名采用 `Nt*` 原生命名,与 `data/` 中的 trace 一致。

### 重新生成

这些产物是脚本生成的,不要手工编辑。若要修改映射,请改对应
`source_md/` 笔记里的 `## 总结` 汇总表,然后重新运行:

```bash
python3 reference/build_reference.py
```

### 统计

12 个模块 · 131 个函数 · 208 个 (函数, 系统调用) 对。

| 模块 | 函数数 | | 模块 | 函数数 |
| --- | --- | --- | --- | --- |
| `os` | 36 | | `time` | 12 |
| `socket` | 43 | | `winreg` | 14 |
| `ssl` | 5 | | `uuid` | 5 |
| `mmap` | 4 | | `msvcrt` | 3 |
| `signal` | 3 | | `winsound` | 3 |
| `multiprocessing` | 2 | | `select` | 1 |
