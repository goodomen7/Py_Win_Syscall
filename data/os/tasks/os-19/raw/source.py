import os
import msvcrt
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# os.get_handle_inheritable 接受 Windows HANDLE（整数），不是 fd
tmp = tempfile.NamedTemporaryFile(delete=False)
fd = tmp.fileno()
handle = msvcrt.get_osfhandle(fd)  # fd → Win32 HANDLE

# 触发：NtQueryObject
_xperf_mark("os_get_handle_inheritable__NtQueryObject__BEGIN")
result = os.get_handle_inheritable(handle)
_xperf_mark("os_get_handle_inheritable__NtQueryObject__END")

tmp.close()
os.unlink(tmp.name)
