import os
import msvcrt
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

tmp = tempfile.NamedTemporaryFile(delete=False)
fd = tmp.fileno()
handle = msvcrt.get_osfhandle(fd)  # fd → Win32 HANDLE

# 触发：NtSetInformationObject
_xperf_mark("os_set_handle_inheritable__NtSetInformationObject__BEGIN")
os.set_handle_inheritable(handle, True)
_xperf_mark("os_set_handle_inheritable__NtSetInformationObject__END")

tmp.close()
os.unlink(tmp.name)
