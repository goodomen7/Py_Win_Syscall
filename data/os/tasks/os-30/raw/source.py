import os
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

new_dir = os.path.join(tempfile.gettempdir(), "_xperf_mkdir_test")

# 触发：NtCreateFile
_xperf_mark("os_mkdir__NtCreateFile__BEGIN")
os.mkdir(new_dir)
_xperf_mark("os_mkdir__NtCreateFile__END")

os.rmdir(new_dir)
