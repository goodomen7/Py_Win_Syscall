import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.write(b"data to sync")
fd = tmp.fileno()

# 触发：NtFlushBuffersFile
_xperf_mark("os_fsync__NtFlushBuffersFile__BEGIN")
os.fsync(fd)
_xperf_mark("os_fsync__NtFlushBuffersFile__END")

tmp.close()
os.unlink(tmp.name)
