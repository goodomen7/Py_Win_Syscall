#!/usr/bin/env python3
"""Build the static "stdlib function -> Windows NtAPI" truth map from the
research markdown notes in ``source_md/``.

Each source ``.md`` file documents one Python standard-library module. The
authoritative mapping lives in that file's ``## 总结`` (summary) table:

    | # | 函数 | 系统调用名 | 条件 |

where one function may span several rows (a blank 函数 cell continues the
function above) and one cell may list several syscalls separated by ``<br>``.

This script flattens those tables into three artifacts in this directory:

    ground_truth.jsonl   one record per function (primary, machine-readable)
    ground_truth.json    same records grouped by library (for browsing)
    ground_truth.csv     one row per (function, syscall) pair (for spreadsheets)

Run from anywhere:  python3 reference/build_reference.py
"""
import csv
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(HERE, "source_md")


def clean_md(s: str) -> str:
    """Strip light markdown (backticks, bold) but keep the text."""
    s = s.replace("**", "").replace("`", "")
    return s.strip()


def strip_code(s: str) -> str:
    return s.strip().strip("`").strip()


def split_row(line: str):
    parts = line.split("|")
    if parts and parts[0].strip() == "":
        parts = parts[1:]
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    return [p.strip() for p in parts]


def is_sep(cells):
    return bool(cells) and all(
        re.fullmatch(r":?-{2,}:?", c) for c in cells if c != ""
    )


def lib_name(path: str) -> str:
    m = re.search(r"windows_(.+?)库", os.path.basename(path))
    return m.group(1) if m else os.path.splitext(os.path.basename(path))[0]


def parse_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    idx = text.find("## 总结")
    if idx == -1:
        return []
    lines = text[idx:].splitlines()
    rows = [l for l in lines if l.lstrip().startswith("|")]
    if not rows:
        return []

    header_cells = None
    seen_sep = False
    data_rows = []
    for r in rows:
        cells = split_row(r)
        if is_sep(cells):
            seen_sep = True
            continue
        if header_cells is None:
            header_cells = cells
            continue
        if seen_sep:
            data_rows.append(cells)

    def col_of(*names):
        for i, h in enumerate(header_cells):
            if any(n in h for n in names):
                return i
        return None

    c_func = col_of("函数")
    c_sys = col_of("系统调用")
    c_cond = col_of("条件", "摘要")

    lib = lib_name(path)
    src = os.path.basename(path)
    results = []
    seq = 0
    current = None
    for cells in data_rows:
        def get(i):
            return cells[i] if (i is not None and i < len(cells)) else ""

        func = strip_code(get(c_func))
        sys_cell = get(c_sys)
        cond_raw = clean_md(get(c_cond))
        cond = cond_raw or None

        if func:
            func = re.sub(r"\(\s*\)$", "", func)
            if "." not in func:
                func = f"{lib}.{func}"
            seq += 1
            current = {
                "id": f"{lib}-{seq:02d}",
                "library": lib,
                "function": func,
                "syscalls": [],
                "source": src,
            }
            results.append(current)
        if current is None:
            continue
        for piece in re.split(r"<br\s*/?>", sys_cell):
            raw = strip_code(piece).strip()
            if not raw:
                continue
            entry = {"name": raw, "condition": cond}
            # Some names carry an info-class argument, e.g.
            # "NtQueryInformationProcess(ProcessTimes)" -> name + arg.
            m = re.fullmatch(r"(Nt[A-Za-z0-9]+)\(([^)]*)\)", raw)
            if m:
                entry["name"] = m.group(1)
                arg = m.group(2).strip()
                if arg:
                    entry["arg"] = arg
            current["syscalls"].append(entry)
    return results


def main():
    records = []
    for path in sorted(glob.glob(os.path.join(SRC_DIR, "*.md"))):
        records.extend(parse_file(path))

    with open(os.path.join(HERE, "ground_truth.jsonl"), "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    by_lib = {}
    for r in records:
        by_lib.setdefault(r["library"], []).append(
            {k: v for k, v in r.items() if k not in ("library", "source")}
        )
    with open(os.path.join(HERE, "ground_truth.json"), "w", encoding="utf-8") as f:
        json.dump(by_lib, f, ensure_ascii=False, indent=2)

    with open(os.path.join(HERE, "ground_truth.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "library", "function", "syscall", "condition"])
        for r in records:
            if not r["syscalls"]:
                w.writerow([r["id"], r["library"], r["function"], "", ""])
            for s in r["syscalls"]:
                w.writerow([r["id"], r["library"], r["function"], s["name"], s["condition"] or ""])

    libs = sorted(by_lib)
    pairs = sum(len(r["syscalls"]) for r in records)
    print(f"libraries: {len(libs)}  functions: {len(records)}  pairs: {pairs}")
    for lib in libs:
        print(f"  {lib}: {len(by_lib[lib])}")


if __name__ == "__main__":
    main()
