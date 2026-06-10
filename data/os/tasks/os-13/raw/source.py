import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.write(b"hello world")
tmp.close()

fd = os.open(tmp.name, os.O_RDONLY)

# 触发：NtReadFile
_xperf_mark("os_read__NtReadFile__BEGIN")
data = os.read(fd, 11)
_xperf_mark("os_read__NtReadFile__END")

os.close(fd)
os.unlink(tmp.name)
