import time
import sys
import os
import uuid

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- uuid.uuid5() ---
# uuid5需要命名空间和名字
namespace = uuid.NAMESPACE_DNS
name = "example.com"

_xperf_mark("BEGIN")
result = uuid.uuid5(namespace, name)
_xperf_mark("END")

print(f"uuid.uuid5('{namespace}', '{name}') result: {result}")