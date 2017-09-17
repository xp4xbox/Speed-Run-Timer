# Speed-Run-Timer

This is a timer/stopwatch made in python for timing speed runs in games and record them for later viewing. Includes a customizable icon, title, ect.

![alt text](https://i.imgur.com/wRpzn71.png)

Requires Python 3, PyHook and Pywin32

## Building Instructions For Pyinstaller

1. Remove line 195 in the program (root.iconbitmap("toad.ico")) 
##### NOTE: This step is optional although the file will no longer be a standalone .exe.

2. Run pyinstaller SpeedRunTimer.py --onefile --windowed --icon=PATHHERE
