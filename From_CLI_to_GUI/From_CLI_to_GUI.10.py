"""
Display the sum of two integers when a button is pressed.

Usage: From_CLI_to_GUI.10.py
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

        self.btn_sum = Button(frame, text="+", width=10, command=self.do_sum)
        self.btn_sum.pack(side=LEFT)

    def do_sum(self):
        int1 = self.integer1.get()
        int1 = self.str_to_int(int1)
        int2 = self.integer2.get()
        int2 = self.str_to_int(int2)
        if int1 is None or int2 is None:
            print('Sorry, need two integer strings.')
        else:
            the_sum = int1 + int2
            print(f'The sum of {int1} and {int2} is {the_sum}')

    def str_to_int(self, value):
        """Get an integer from a string.  Return None if can't get integer."""

        try:
            result = int(value)
            return result
        except ValueError:
            return None

root = Tk()
app = App(root)
root.mainloop()
