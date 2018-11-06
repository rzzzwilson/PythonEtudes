"""
Display the sum of two integers when a button is pressed.

Usage: From_CLI_to_GUI.8.py
"""

from tkinter import *       # this is bad practice, see later examples

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.integer1 = Entry(frame)
        self.integer1.pack(side=LEFT)

        self.integer2 = Entry(frame)
        self.integer2.pack(side=LEFT)

        self.btn_sum = Button(frame, text="+")
        self.btn_sum.pack(side=LEFT)

root = Tk()
app = App(root)
root.mainloop()
