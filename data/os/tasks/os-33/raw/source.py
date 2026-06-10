import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass


open("src.txt", "w").close()
open("dst.txt", "w").close()

_xperf_mark("_BEGIN")
os.replace("src.txt", "dst.txt")   # 原子覆盖 dst
_xperf_mark("_END")
