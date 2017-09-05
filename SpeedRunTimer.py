from tkinter import *
import tkinter as tk
import tkinter.messagebox
import time
import os.path
from heapq import nsmallest
import pyHook

def OnKeyboardEvent(event):
    if event.Key == "Space":
        btnStopState = str(btnStop["state"])
        if not btnStopState == "disabled":
            OnClickButtonStop()
    return True

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()

strStop = "no"

strOutput = "00:00.00.00"

def ResetStop():
    global strStop; strStop = "no"

def OnClickButtonStart():
    btnStop.configure(state="active")
    btnStart.configure(state="disabled")
    btnReset.configure(state="disabled")
    global strOutput
    if strOutput == "00:00.00.00":
        global intTimeSec; intTimeSec = 0
        global intTimeMin; intTimeMin = 0
        global intTimeHour; intTimeHour = 0
        global intTime; intTime = 0
    blnTrueFalse = format(delay.get())
    if str(blnTrueFalse) == "True":
        time.sleep(5)
    while True:
        if strStop == "yes":
            break
        time.sleep(0.01)
        intTime += 1
        if intTime > 99:
            intTimeSec += 1
            intTime = 0
        if intTimeSec > 59:
            intTimeMin += 1
            intTimeSec = 0
        if intTimeMin > 59:
            intTimeHour += 1
            intTimeMin = 0
        if intTimeSec < 10:
            strTimeSec = "0"+str(intTimeSec)
        else:
            strTimeSec = str(intTimeSec)
        if intTimeMin < 10:
            strTimeMin = "0"+str(intTimeMin)
        else:
            strTimeMin = str(intTimeMin)
        if intTimeHour < 10:
            strTimeHour = "0"+str(intTimeHour)
        else:
            strTimeHour = str(intTimeHour)
        if intTime < 10:
            strTime = "0"+str(intTime)
        else:
            strTime = str(intTime)
        strOutput = (strTimeHour+":"+strTimeMin+"."+strTimeSec+"."+strTime)

        global intTime1; intTime1 = intTime
        global intTimeSec1; intTimeSec1 = intTimeSec
        global intTimeMin1; intTimeMin1 = intTimeMin
        global intTimeHour1; intTimeHour1 = intTimeHour

        lbtime["text"] = strOutput
        Tk.update(root)
    ResetStop()
    btnStart.configure(state="normal")

def OnClickButtonReset():
    lbtime["text"] = "00:00.00.00"
    global strOutput; strOutput = "00:00.00.00"
    Tk.update(root)
    btnReset.configure(state="disabled")
    global intTimeSec; intTimeSec = 0
    global intTimeMin; intTimeMin = 0
    global intTimeHour; intTimeHour = 0
    global intTime; intTime = 0

def OnClickButtonStop():
    global strStop; strStop = "yes"
    btnStop.configure(state="disabled")
    btnReset.configure(state="normal")

def BestTime():
    if os.path.isfile("times.txt") == True:
        aLinesSpace = []
        objFile = open("times.txt", "r")
        aLines = objFile.readlines()
        for intCounter in aLines:
            j = intCounter.replace(".","")
            j = j.replace(":","")
            j = j.replace("\n","")
            aLinesSpace.append(j)
        while len(aLinesSpace) < 5:
            # dummy values
            aLinesSpace.append("999999999")
        # get correct format
        Time1 = (nsmallest(5, aLinesSpace)[0])
        Time1 = Time1[0:2]+":"+Time1[2:4]+"."+Time1[4:6]+"."+Time1[6:8]
        if Time1 == "99:99.99.99": Time1 = "\t   "
        Time2 = (nsmallest(5, aLinesSpace)[1])
        Time2 = Time2[0:2] + ":" + Time2[2:4] + "." + Time2[4:6] + "." + Time2[6:8]
        if Time2 == "99:99.99.99": Time2 = "\t   "
        Time3 = (nsmallest(5, aLinesSpace)[2])
        Time3 = Time3[0:2] + ":" + Time3[2:4] + "." + Time3[4:6] + "." + Time3[6:8]
        if Time3 == "99:99.99.99": Time3 = "\t   "
        Time4 = (nsmallest(5, aLinesSpace)[3])
        Time4 = Time4[0:2] + ":" + Time4[2:4] + "." + Time4[4:6] + "." + Time4[6:8]
        if Time4 == "99:99.99.99": Time4 = "\t   "
        Time5 = (nsmallest(5, aLinesSpace)[4])
        Time5 = Time5[0:2] + ":" + Time5[2:4] + "." + Time5[4:6] + "." + Time5[6:8]
        if Time5 == "99:99.99.99": Time5 = "\t   "

    window = tk.Toplevel()
    window.geometry("200x180")
    window.resizable(0,0)
    window.title("Best Times")

    def OnClickButtonOK():
        window.destroy()

    def OnClickButtonClear():
        open("times.txt", "w").close()
        window.destroy()

    lbtitle = Label(window, text="Rank\t\t\tTime"); lbtitle.pack(side=TOP, expand=True)
    lbtitle2 = Label(window, text="1\t\t"+Time1); lbtitle2.pack()
    lbtitle3 = Label(window, text="2\t\t" + Time2); lbtitle3.pack()
    lbtitle4 = Label(window, text="3\t\t" + Time3); lbtitle4.pack()
    lbtitle5 = Label(window, text="4\t\t" + Time4); lbtitle5.pack()
    lbtitle6 = Label(window, text="5\t\t" + Time5); lbtitle6.pack()
    btnClear = Button(window, text="Clear", width=7, height=0, bd=3, command=OnClickButtonClear)
    btnClear.pack(side=RIGHT, expand=True)
    btnOK = Button(window, text="OK", width=7, height=0, bd=3, command=OnClickButtonOK)
    btnOK.pack(side=BOTTOM, expand=True, padx=18)

def SaveToLog():
    if strOutput == "00:00.00.00":
        tkinter.messagebox.showerror("Error", "The Timer Is At 0!")
    else:
        if os.path.isfile("times.txt") == False:
            objFile = open("times.txt", "w")
        else:
            objFile = open("times.txt", "a")
        if strOutput == "99:99.99.99":
            objFile.write("99:99.99.98")
        else:
            objFile.write(strOutput)
        objFile.write("\n")
        objFile.close()

def ChangeIcon():
    window3 = tk.Toplevel()
    window3.resizable(0, 0)

    EntryIcon = Entry(window3)
    EntryIcon.insert(END, "Path to icon")
    EntryIcon.pack()
    EntryIcon.focus_set()

    def callback2():
        strEntry = EntryIcon.get()
        try:
            root.iconbitmap(strEntry)
        except TclError:
            tkinter.messagebox.showerror("Error", "Invalid Path/Icon")
        window3.destroy()

    ButtonIcon = Button(window3, text="OK", width=10, command=callback2)
    ButtonIcon.pack()

def ChangeTitle():
    window2 = tk.Toplevel()
    window2.resizable(0, 0)

    EntryTitle = Entry(window2)
    EntryTitle.pack()
    EntryTitle.focus_set()

    def callback():
        strTitle = EntryTitle.get()
        root.wm_title(strTitle)
        window2.destroy()

    ButtonTitle = Button(window2, text="OK", width=10, command=callback)
    ButtonTitle.pack()

root = Tk()

root.resizable(0, 0)
root.wm_title("Battletoads Timer")
root.geometry("250x100")
root.iconbitmap("toad.ico")


lbtime = Label(root, pady=10, text=strOutput)
lbtime.config(font=("TkDefaultFont", 16)); lbtime.pack()

btnStart = Button(root, text="Start", width=7, bd=3, pady=-1, padx=4, command=OnClickButtonStart); btnStart.pack(side=LEFT, expand=True)
btnStop = Button(root, text="Stop", width=7, bd=3, pady=-1, padx=4, command=OnClickButtonStop); btnStop.pack(side=LEFT, expand=True)
btnReset = Button(root, text="Reset", width=7, bd=3, pady=-1, padx=4, command=OnClickButtonReset); btnReset.pack(side=LEFT, expand=True)
btnStop.configure(state="disabled")
btnReset.configure(state="disabled")

Menu1 = Menu(root)
root.config(menu=Menu1)
SubMenu = Menu(Menu1, tearoff=False)
SubMenu2 = Menu(Menu1, tearoff=False)
Menu1.add_cascade(label="Times", menu=SubMenu)
Menu1.add_cascade(label="Options", menu=SubMenu2)
SubMenu.add_command(label="Save Time", command=SaveToLog)
SubMenu.add_command(label="Best Times", command=BestTime)
delay = tk.BooleanVar()
delay.set(False)
SubMenu2.add_checkbutton(label="5 Second Delay Start", variable=delay)
SubMenu2.add_command(label="Change Title", command=ChangeTitle)
SubMenu2.add_command(label="Change Icon", command=ChangeIcon)

root.mainloop()
