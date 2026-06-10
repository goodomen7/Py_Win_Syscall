import mmap

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

_m_resize = mmap.mmap(-1, 4096)

_xperf_mark("BEGIN")
_m_resize.resize(8192)
_xperf_mark("END")