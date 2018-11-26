## Tkinter ##

try:
    import tkinter
except ImportError:             # Python 2
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+350+100')

label = tkinter.Label(mainWindow, text="Hello World")
label.pack(side='top')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

button1 = tkinter.Button(rightFrame, text='Button 1')
button2 = tkinter.Button(rightFrame, text='Button 2')
button3 = tkinter.Button(rightFrame, text='Button 3')
# button1.pack(side='left', anchor='n')       # anchor only affecting vertical positions here
# button1.pack(side='top', anchor='n')          # anchor only affecting horizontal positions here
# button2.pack(side='top', anchor='s')
# button3.pack(side='top', anchor='e')
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainWindow.mainloop()

## Pack is only suitable for simple layouts, it is limited!