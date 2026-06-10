import mmap
import os
import tempfile


def _xperf_mark(name):
    try:
        open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError:
        pass


# 1. 创建一个临时文件（让 mmap 持有 file_handle）
with open("tmp.bin", "wb") as f:
    f.write(b"\x00" * 1024)

# 2. 用文件映射打开 mmap（关键：必须传文件的 fileno，而非 -1）
with open("tmp.bin", "r+b") as f:
    with mmap.mmap(f.fileno(), 0) as m:
        _xperf_mark("BEGIN")
        size = m.size()  # ← 触发 NtQueryInformationFile
        _xperf_mark("END")
        print(size)  # 1024