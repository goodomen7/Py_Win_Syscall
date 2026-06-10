import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass


open("stat_target.txt", "w").close()

_xperf_mark("_BEGIN")
os.stat("stat_target.txt")
_xperf_mark("_END")
