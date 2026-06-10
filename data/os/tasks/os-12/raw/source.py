import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：NtCreateNamedPipeFile + NtOpenFile
_xperf_mark("os_pipe__NtCreateNamedPipeFile_NtOpenFile__BEGIN")
r, w = os.pipe()
_xperf_mark("os_pipe__NtCreateNamedPipeFile_NtOpenFile__END")

os.close(r)
os.close(w)
