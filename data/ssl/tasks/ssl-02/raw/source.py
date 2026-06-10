import ssl
import sys
import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- ssl.cert_time_to_seconds ---
test_time = "May  9 00:00:00 2023 GMT"
_xperf_mark("BEGIN")
result = ssl.cert_time_to_seconds(test_time)
_xperf_mark("END")