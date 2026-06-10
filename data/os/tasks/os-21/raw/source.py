import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.close()

# 触发：NtQueryAttributesFile + NtCreateFile
_xperf_mark("os_access__NtQueryAttributesFile_NtCreateFile__BEGIN")
os.access(tmp.name, os.R_OK)
_xperf_mark("os_access__NtQueryAttributesFile_NtCreateFile__END")

os.unlink(tmp.name)
