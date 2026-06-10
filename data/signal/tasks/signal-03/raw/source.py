import time
import sys
import os
import signal

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- signal.signal (内部触发 NtRequestWaitReplyPort) ---
def handler(signum, frame):
    print(f"收到信号: {signum}")

# 注册信号处理器
original_handler = signal.signal(signal.SIGINT, handler)
print(f"注册信号处理器成功，原处理器: {original_handler}")
# 恢复原处理器
_xperf_mark("BEGIN")
signal.signal(signal.SIGINT, original_handler)
_xperf_mark("END")