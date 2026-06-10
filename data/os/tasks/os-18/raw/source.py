import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp = tempfile.NamedTemporaryFile(delete=False)
fd = tmp.fileno()

# 触发：NtSetInformationObject
_xperf_mark("os_set_inheritable__NtSetInformationObject__BEGIN")
os.set_inheritable(fd, True)
_xperf_mark("os_set_inheritable__NtSetInformationObject__END")

tmp.close()
os.unlink(tmp.name)
