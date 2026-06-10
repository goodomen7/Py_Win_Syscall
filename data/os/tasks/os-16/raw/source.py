import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp_path = tempfile.mktemp(suffix=".tmp")
fd = os.open(tmp_path, os.O_CREAT | os.O_WRONLY)

# 触发：NtWriteFile
_xperf_mark("os_write__NtWriteFile__BEGIN")
os.write(fd, b"hello world")
_xperf_mark("os_write__NtWriteFile__END")

os.close(fd)
os.unlink(tmp_path)
