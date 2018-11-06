"""
Display the sum of two integers when a button is pressed.

Usage: From_CLI_to_GUI.9.py
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

        self.do_sum = Button(frame, text="+", width=10, command=self.do_sum)
        self.do_sum.pack(side=LEFT)

    def do_sum(self):
        int1 = self.integer1.get()      # get the text in the first Entry box
        int1 = int(int1)                # convert string to int
        int2 = self.integer2.get()
        int2 = int(int2)
        the_sum = int1 + int2
        print(f'The sum of {int1} and {int2} is {the_sum}')

root = Tk()
app = App(root)
root.mainloop()
