import ssl
import sys
import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- ssl.enum_certificates ---
_xperf_mark("BEGIN")
certs = ssl.enum_certificates("ROOT")
_xperf_mark("END")