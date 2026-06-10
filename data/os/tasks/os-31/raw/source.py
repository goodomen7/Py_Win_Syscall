import os
import shutil
import tempfile

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

nested = os.path.join(tempfile.gettempdir(), "_xperf_makedirs_a", "b", "c")

# makedirs 为每一层目录调用 NtCreateFile
# 触发：NtCreateFile（每级目录各一次）
_xperf_mark("os_makedirs__NtCreateFile__BEGIN")
os.makedirs(nested)
_xperf_mark("os_makedirs__NtCreateFile__END")

shutil.rmtree(os.path.join(tempfile.gettempdir(), "_xperf_makedirs_a"))
