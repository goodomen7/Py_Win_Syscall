import time
import sys
import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- time.sleep ---

_xperf_mark("BEGIN")
time.sleep(0.001)
_xperf_mark("END")
