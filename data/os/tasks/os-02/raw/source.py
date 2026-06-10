import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

_orig = os.getcwd()

# 触发：NtOpenFile + NtQueryVolumeInformationFile + NtClose
_xperf_mark("os_chdir__NtOpenFile_NtQueryVolumeInformationFile_NtClose__BEGIN")
os.chdir("C:\\")
_xperf_mark("os_chdir__NtOpenFile_NtQueryVolumeInformationFile_NtClose__END")
