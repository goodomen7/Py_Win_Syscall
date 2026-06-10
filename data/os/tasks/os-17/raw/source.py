import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp = tempfile.NamedTemporaryFile(delete=False)
fd = tmp.fileno()

# 触发：NtQueryObject
_xperf_mark("os_get_inheritable__NtQueryObject__BEGIN")
result = os.get_inheritable(fd)
_xperf_mark("os_get_inheritable__NtQueryObject__END")

tmp.close()
os.unlink(tmp.name)
