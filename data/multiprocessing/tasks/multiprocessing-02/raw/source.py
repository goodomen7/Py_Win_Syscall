import time
import sys
import os
import multiprocessing

def _xperf_mark(name):
    try:
        open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError:
        pass

# --- multiprocessing.cpu_count ---
_xperf_mark("BEGIN")
cpu_count = multiprocessing.cpu_count()  # 触发系统调用
_xperf_mark("END")
