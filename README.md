# Speed-Run-Timer

This is a timer/stopwatch made in python for timing speed runs in games and record them for later viewing.

The default title for the program is Battletoads Timer although it can be changed either permanently in the code or in the program itself. Same goes with the icon.

![alt text](https://i.imgur.com/wRpzn71.png)

Requires Python 3, PyHook and Pywin32

## BUILDING INSTRUCTIONS FOR PYINSTALLER:

1. Remove line 195 in the program (root.iconbitmap("toad.ico"))
2. Run pyinstaller SpeedRunTimer.py --onefile --windowed --icon=PATHHERE
