import ssl
import sys
import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- ssl.enum_crls ---
_xperf_mark("BEGIN")
crls = ssl.enum_crls("ROOT")
_xperf_mark("END")
_xperf_mark("END")