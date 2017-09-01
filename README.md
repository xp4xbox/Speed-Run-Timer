# Simple-Speed-Run-Timer

This is a simple timer/stopwatch made in python for timing speed runs in games and record them for later viewing. Requires no aditional modules other than the default ones in python3. 

The default title for the program is Battletoads Timer although it can be changed either permanently in the code or in the program itself. Same goes with the icon.

BUILDING INSTRUCTIONS FOR PYINSTALLER:

1. Remove line 195 in the program (root.iconbitmap("toad.ico"))
2. Run pyinstaller SpeedRunTimer.py --onefile --windowed --icon=<ICON PATH HERE>
