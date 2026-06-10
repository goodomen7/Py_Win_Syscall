import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp = tempfile.NamedTemporaryFile(delete=False)
fd = tmp.fileno()

# 触发：NtQueryInformationFile + NtSetInformationFile
_xperf_mark("os_fchmod__NtQueryInformationFile_NtSetInformationFile__BEGIN")
os.fchmod(fd, 0o644)
_xperf_mark("os_fchmod__NtQueryInformationFile_NtSetInformationFile__END")
