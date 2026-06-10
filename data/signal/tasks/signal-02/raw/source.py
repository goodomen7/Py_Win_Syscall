import time
import sys
import os
import signal

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- signal.set_wakeup_fd (内部触发 NtDeviceIoControlFile) ---

import socket
sock1, sock2 = socket.socketpair()
try:
    _xperf_mark("BEGIN")
    old_fd = signal.set_wakeup_fd(sock1.fileno())
    _xperf_mark("END")
    print(f"设置 wakeup fd 成功，原 fd: {old_fd}")
finally:
    # 恢复原设置
    signal.set_wakeup_fd(old_fd)
    sock1.close()
    sock2.close()
