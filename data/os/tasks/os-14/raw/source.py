import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass



# 先创建：
# mklink test_link.txt target.txt  (cmd, 管理员)

_xperf_mark("os_readinto__NtReadFile__BEGIN")
os.readlink("test_link.txt")
_xperf_mark("os_readinto__NtReadFile__END")