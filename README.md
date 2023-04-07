# dont_sleep_lock

Uses windll from ctypes


## README.md was generated using ChatGPT

Dont_Sleep_Lock

This script prevents your computer from going into sleep mode or locking the screen due to inactivity. It simulates user activity by moving the mouse cursor every 2 minutes.
Requirements

    Python 3.x
    ctypes module

Usage

    Download the "dont_sleep_lock.py" file from this repository to your computer.
    Open a terminal and navigate to the directory where you saved the file.
    Run the script by typing python dont_sleep_lock.py in the terminal.
    To stop the script, press ctrl-c.

Explanation of Code

```python

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
```

The ctypes module provides a way to call functions in shared libraries that are written in C. We use it to call the mouse_event function from the Windows API.
The time module is used to pause the execution of the script for a specified number of seconds.
The mouse_event function simulates a mouse event such as a button click or movement.
The MOUSEEVENTF_MOVE constant is passed to the mouse_event function to indicate that we want to move the mouse cursor.
The try block contains a loop that executes indefinitely until the script is stopped by the user.
Inside the loop, we simulate movement of the mouse cursor by calling mouse_event with different parameters to move the cursor up, down, left, and right.
The time.sleep function is used to pause the execution of the script for 2 minutes between each mouse movement.
The except block catches the KeyboardInterrupt exception which is raised when the user presses ctrl-c to stop the script.
