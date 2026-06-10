import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：内部调用 gethostname(NtOpenKey+NtQueryValueKey) + gethostbyaddr(NtDeviceIoControlFile)
_xperf_mark("getfqdn_BEGIN")
fqdn = socket.getfqdn()
_xperf_mark("getfqdn_END")
