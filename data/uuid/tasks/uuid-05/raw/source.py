import time
import sys
import os
import uuid

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- uuid.getnode() ---
_xperf_mark("BEGIN")
result = uuid.getnode()
_xperf_mark("END")

print(f"uuid.getnode() result: {result} (MAC address as integer)")
print(f"MAC address (hex): {':'.join(format((result >> i) & 0xFF, '02x') for i in range(40, -1, -8))}")