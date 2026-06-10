import time
import sys
import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- time.localtime ---

_xperf_mark("BEGIN")
time.localtime(-1)
_xperf_mark("END")
