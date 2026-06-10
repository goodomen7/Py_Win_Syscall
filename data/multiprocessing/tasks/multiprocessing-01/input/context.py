import time
import sys
import os
import multiprocessing

def dummy_worker():
    time.sleep(0.1)

p = multiprocessing.Process(target=dummy_worker)
p.start()

time.sleep(0.3)

children = multiprocessing.active_children()  # → poll() → NtQueryInformationProcess

cpu_count = multiprocessing.cpu_count()  # 触发系统调用