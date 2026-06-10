import time
import sys
import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- time.thread_time ---

_xperf_mark("BEGIN")
time.thread_time()
_xperf_mark("END")
