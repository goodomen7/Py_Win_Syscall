import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp_path = tempfile.mktemp(suffix=".tmp")

# 触发：NtCreateFile
_xperf_mark("os_open__NtCreateFile__BEGIN")
fd = os.open(tmp_path, os.O_CREAT | os.O_WRONLY)
_xperf_mark("os_open__NtCreateFile__END")

os.close(fd)
os.unlink(tmp_path)
