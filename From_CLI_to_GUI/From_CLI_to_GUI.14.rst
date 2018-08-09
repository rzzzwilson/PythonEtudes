Better GUI design
-----------------

In the previous program we popped up a dialog box to either display the
results or to indicate the user did something wrong.  It's usually better
to display results in the GUI and reserve the dialog approach for some
serious error or when the user has to make a decision (eg, overwrite file?).

We only need to display a single number so we could change the GUI screen to
include a Label whose text we can update to show a valid result.  The program
now looks like:

    """
    Display the sum of two integers when a button is pressed.

    Usage: From_CLI_to_GUI.12.py
    """

    from tkinter import Tk, Frame, Entry, Button, Label, LEFT, BOTTOM, X, messagebox

    class App:
        def __init__(self, master):
            frame = Frame(master)
            frame.pack()

            self.integer1 = Entry(frame, width=10)
            self.integer1.pack(side=LEFT)

            label = Label(frame, text='+', width=3)
            label.pack(side=LEFT)

            self.integer2 = Entry(frame, width=10)
            self.integer2.pack(side=LEFT)

            self.do_sum = Button(frame, text='=', width=3, command=self.do_sum)
            self.do_sum.pack(side=LEFT)

            self.result = Label(master)     # label to hold the result
            self.result.pack(side=BOTTOM, fill=X)

        def do_sum(self):
            # clear previous result
            self.result['text'] = ''

            int1 = self.integer1.get()
            int1 = self.str_to_int(int1)
            int2 = self.integer2.get()
            int2 = self.str_to_int(int2)
            if int1 is None or int2 is None:
                self.error('Sorry, need two integer strings.')
            else:
                the_sum = int1 + int2
                self.result['text'] = f'The sum of {int1} and {int2} is {the_sum}'

        def str_to_int(self, value):
            """Get an integer from a string.  Return None if can't get integer."""

            try:
                result = int(value)
                return result
            except ValueError:
                return None

        def error(self, msg):
            """Display an error message."""

            messagebox.showerror('Error', msg)

    root = Tk()
    app = App(root)
    root.mainloop()

We had to do some tkinter magic to make the widgets display nicely.  Just ignore
the `width=` parameters, etc.  This isn't an etude on tkinter!

Note that we no longer need the `self.info()` routine.

On the
`next page <https://github.com/rzzzwilson/PythonEtudes/wiki/From_CLI_to_GUI.14>`_
we will discuss some more advanced GUI design.
