"""
Display the sum of two integers when a button is pressed.

Usage: From_CLI_to_GUI.13.py
"""

from tkinter import Tk, Frame, Entry, Button, Label, GROOVE

class App:
    def __init__(self, master):
        """Define the GUI screen."""

        self.master = master
        frame = Frame(master)
        frame.grid(column=0, row=0)

        val = master.register(self.validate_int)

        self.integer1 = Entry(frame, width=10, validate='key', vcmd=(val, '%S'))
        self.integer1.grid(row=0, column=0)

        label = Label(frame, text='+', width=3)
        label.grid(row=0, column=1)

        self.integer2 = Entry(frame, width=10, validate='key', vcmd=(val, '%S'))
        self.integer2.grid(row=0, column=2)

        self.do_sum = Button(frame, text='=', width=3, state='disabled', command=self.do_sum)
        self.do_sum.grid(row=0, column=3)

        # label to hold the result
        self.result = Label(master, width=10, relief=GROOVE)
        self.result.grid(row=0, column=4)

    def validate_int(self, text):
        """Validate an Entry widget text."""

        # run "self.check_valid" after this function since
        # the widget text isn't updated until after this function
        self.master.after(0, self.check_valid)
        return text.isdigit()

    def check_valid(self):
        """Check if Entry widgets contain text.  Enable Button if so."""

        self.result['text'] = ''
        self.do_sum['state'] = 'disabled'
        if self.integer1.get() and self.integer2.get():
            self.do_sum['state'] = 'normal'

    def do_sum(self):
        """Sum the two numbers.  We know both fields are integers."""

        int1 = int(self.integer1.get())
        int2 = int(self.integer2.get())
        the_sum = int1 + int2
        self.result['text'] = f'{the_sum}'


root = Tk()
app = App(root)
root.mainloop()
