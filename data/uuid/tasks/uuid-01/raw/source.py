import time
import sys
import os
import uuid

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- uuid.uuid1() ---
_xperf_mark("BEGIN")
result = uuid.uuid1()
_xperf_mark("END")

print(f"uuid.uuid1() result: {result}")