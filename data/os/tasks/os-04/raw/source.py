import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

_xperf_mark("BEGIN")
os.putenv("BIGENV", "A" * (1024 * 1024))
_xperf_mark("END")

