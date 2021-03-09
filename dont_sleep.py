import ctypes
import time


mouse_event = ctypes.windll.user32.mouse_event
MOUSEEVENTF_MOVE = 0x0001
print("ctrl-c to stop")

try:
    while True:
        mouse_event(MOUSEEVENTF_MOVE,1,0,0,0)
        time.sleep(120)
        mouse_event(MOUSEEVENTF_MOVE,0,1,0,0)
        time.sleep(120)
        mouse_event(MOUSEEVENTF_MOVE,-1,0,0,0)
        time.sleep(120)
        mouse_event(MOUSEEVENTF_MOVE,0,-1,0,0)
        time.sleep(120)
except KeyboardInterrupt:
    pass
