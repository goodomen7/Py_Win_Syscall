import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp = tempfile.NamedTemporaryFile(delete=False)
tmp.write(b"x" * 1024)
fd = tmp.fileno()

# 触发：NtSetInformationFile
_xperf_mark("os_ftruncate__NtSetInformationFile__BEGIN")
os.ftruncate(fd, 512)
_xperf_mark("os_ftruncate__NtSetInformationFile__END")

tmp.close()
os.unlink(tmp.name)
