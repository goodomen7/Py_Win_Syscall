import time
import sys
import os
import signal

def _xperf_mark(name):
    try: open(rf"C:\__XPERF_MARK_{name}__.tmp", "rb")
    except OSError: pass

# --- signal.raise_signal (内部会触发 NtTerminateProcess 等系统调用) ---
try:
    # raise_signal 需要有效的信号编号，使用 SIGINT 作为示例
    # 注意：这会向当前进程发送信号，可能导致程序退出
    _xperf_mark("BEGIN")

    signal.raise_signal(signal.SIGINT)
    _xperf_mark("END")
except Exception as e:
    print(f"捕获到异常（预期行为）: {e}")