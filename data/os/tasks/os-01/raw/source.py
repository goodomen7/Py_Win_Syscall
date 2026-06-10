import os

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# 预填充环境变量，使环境块接近容量上限，再写入大值迫使扩容
for i in range(200):
    os.environ[f"_FILL_{i}"] = "x" * 100

# 场景 A：写操作且环境块需扩容
# 触发：NtQueryVirtualMemory + NtAllocateVirtualMemory + NtFreeVirtualMemory
for i in range(200):
    os.environ[f"_FILL_{i}"] = "x" * 100

_xperf_mark("BEGIN")

try:
    for i in range(200):
        del os.environ[f"_FILL_{i}"]
    os.environ["_TRIGGER_EXPAND"] = "z" * (32767 - len("_TRIGGER_EXPAND") - 1)
except Exception as e:
    print(f"error: {e}")
_xperf_mark("END")