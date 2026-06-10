import socket
def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 触发：WSADuplicateSocketW + WSASocketW -> NtCreateFile(\Device\Afd\Endpoint)
#        + SetHandleInformation -> NtQueryObject + NtSetInformationObject
_xperf_mark("dup_BEGIN")
s2 = s.dup()
_xperf_mark("dup_END")

s2.close()
s.close()
