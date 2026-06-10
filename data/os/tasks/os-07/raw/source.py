import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp = tempfile.NamedTemporaryFile(delete=False)
fd = tmp.fileno()

# 触发：NtQueryInformationFile
_xperf_mark("os_fstat__NtQueryInformationFile__BEGIN")
os.fstat(fd)
_xperf_mark("os_fstat__NtQueryInformationFile__END")

tmp.close()
os.unlink(tmp.name)
