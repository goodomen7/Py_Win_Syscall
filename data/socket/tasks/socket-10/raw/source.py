import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：GetComputerNameExW -> GetComputerNameFromRegistry
#        -> ZwOpenKey(NtOpenKey) + ZwQueryValueKey(NtQueryValueKey)
_xperf_mark("gethostname_BEGIN")
name = socket.gethostname()
_xperf_mark("gethostname_END")
