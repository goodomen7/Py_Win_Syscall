import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmpdir = tempfile.mkdtemp()

# 触发：NtQueryDirectoryFile
_xperf_mark("os_listdir__NtQueryDirectoryFile__BEGIN")
os.listdir(tmpdir)
_xperf_mark("os_listdir__NtQueryDirectoryFile__END")

os.rmdir(tmpdir)
