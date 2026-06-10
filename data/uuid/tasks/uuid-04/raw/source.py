import time
import sys
import os
import uuid

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- uuid.uuid6() ---
# 注意: uuid6需要Python 3.11+或安装uuid6包
# 如果标准库不支持，请运行: pip install uuid6
try:
    # 尝试从标准库导入（Python 3.11+）
    from uuid import uuid6 as uuid6_std
    _xperf_mark("BEGIN")
    result = uuid6_std()
    _xperf_mark("END")
except (ImportError, AttributeError):
    # 回退到uuid6包
    try:
        from uuid6 import uuid6 as uuid6_pkg
        _xperf_mark("BEGIN")
        result = uuid6_pkg()
        _xperf_mark("END")
    except ImportError:
        print("uuid6 not available. Please install: pip install uuid6")
        sys.exit(1)

print(f"uuid.uuid6() result: {result}")