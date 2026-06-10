import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass


os.mkdir("empty_dir")


_xperf_mark("_BEGIN")
os.rmdir("empty_dir")
_xperf_mark("_END")

