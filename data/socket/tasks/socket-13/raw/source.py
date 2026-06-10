import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发：getprotobyname -> RegOpenKeyEx(NtOpenKey) + RegQueryValueEx(NtQueryValueKey)
#        + CreateFile(NtCreateFile) + ReadFile(NtReadFile) 读取 etc/protocol 文件
_xperf_mark("getprotobyname_BEGIN")
p = socket.getprotobyname("tcp")
_xperf_mark("getprotobyname_END")
