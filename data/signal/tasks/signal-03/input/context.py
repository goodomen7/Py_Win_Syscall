import time
import sys
import os
import signal
import socket

signal.raise_signal(signal.SIGINT)

sock1, sock2 = socket.socketpair()
old_fd = signal.set_wakeup_fd(sock1.fileno())
signal.set_wakeup_fd(old_fd)
sock1.close()
sock2.close()

def handler(signum, frame):
    pass

original_handler = signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGINT, original_handler)