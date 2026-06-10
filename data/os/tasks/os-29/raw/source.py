import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.close()

# 触发：NtCreateFile + NtQueryInformationFile
_xperf_mark("os_lstat__NtCreateFile_NtQueryInformationFile__BEGIN")
os.lstat(tmp.name)
_xperf_mark("os_lstat__NtCreateFile_NtQueryInformationFile__END")

os.unlink(tmp.name)
