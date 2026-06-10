import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.close()

# 触发：NtOpenFile + NtSetInformationFile
_xperf_mark("os_chmod__NtOpenFile_NtSetInformationFile__BEGIN")
os.chmod(tmp.name, 0o644)
_xperf_mark("os_chmod__NtOpenFile_NtSetInformationFile__END")

os.unlink(tmp.name)
