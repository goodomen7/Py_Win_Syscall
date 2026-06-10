import time
import sys
import os
import multiprocessing

def _xperf_mark(name):
    try:
        open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError:
        pass

# --- multiprocessing.active_children ---
_xperf_mark("BEGIN")
children = multiprocessing.active_children()  # 触发系统调用
_xperf_mark("END")
