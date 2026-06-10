import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 触发条件：首次调用
# 触发：NtQueryInformationProcess
_xperf_mark("os_getppid__NtQueryInformationProcess__BEGIN")
ppid = os.getppid()
_xperf_mark("os_getppid__NtQueryInformationProcess__END")
