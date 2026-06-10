import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# os.listdrives() 为 Python 3.12+ Windows 专有函数
# 触发：NtQueryInformationProcess
_xperf_mark("os_listdrives__NtQueryInformationProcess__BEGIN")
drives = os.listdrives()
_xperf_mark("os_listdrives__NtQueryInformationProcess__END")
