import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass


_xperf_mark("_BEGIN")
with os.scandir(".") as it:
    _xperf_mark("_END")
    for entry in it:   
         pass