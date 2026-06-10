import ssl
import sys
import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- ssl.create_default_context ---
_xperf_mark("BEGIN")
context = ssl.create_default_context()
_xperf_mark("END")