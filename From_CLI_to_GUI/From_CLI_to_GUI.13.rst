Better GUI design
-----------------

The previous program displays a messagebox dialog when the user makes
a mistake, like leaving one integer Entry widget empty or not putting an integer
into an Entry widget.  This is fine, but a better approach is to not tell the
user they made a mistake, but to *not allow them* to make a mistake.

In this program the two mistakes the user can make are:

* press the "=" button when one or more Entry widgets are empty, and
* enter a non-integer string into an Entry widget.

Not allowing the user to press the "=" button when one or more Entry widgets
are empty is easy: we just disable the button until both widgets are non-empty.
How we do that is dependant on the particular GUI framework used, but for all
of them we must have logic that checks both widgets whenever there is a change
in either of them, and set the state of the Button accordingly.  In this program
the `check_valid()` function does all the work.  We just have to call the
function at the appropriate times.

Not allowing the user to enter invalid characters into either Entry widget is
more difficult, but most GUI frameworks have the idea of a validation function
that can control what the user can enter in a text widget.  Again, the actual
details vary with the GUI framework used.  In the program the `validate_int()`
function does the validation.

The final program is::

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

Note that we no longer have any error messages.  The user can't make a mistake
and the program is more user-friendly.

When we run the program note that the "=" button is disables - trying to press
it does nothing.  Here is the program after we have entered one number only:

.. image:: From_CLI_to_GUI/From_CLI_to_GUI.13.0.png

The button is disabled and when you try to enter "abc" into the other Entry
widget nothing happens.  Non-digit characters are ignored!

We've come a long way from the initial program::

    """
    Prompt the user for two integer numbers and print the sum.
    """
    
    int1 = input('Enter the first integer: ')
    int2 = input('Enter the second integer: ')
    the_sum = int1 + int2
    print(f'The sum of {int1} and {int2} is {the_sum}')

The amount of code you have to write to make a GUI application pleasant and
easy to use is not insignificant, but it's worth it!

What next?
----------

Our "add two numbers" program isn't complete.  What program ever is?  Here are a
few suggestions for improvement.

We can't input a negative integer.  That wouldn't be hard to add - we just need
to make the `check_valid()` function handle an optional leading "-" sign.  Or
maybe a better idea is to change the code in the `check_valid()` function 
completely.  Just try to convert the text string to an int and return False
if we can't.

We should allow floating point numbers.  Again, modify `check_valid()` to allow
floats and change the `int()` calls in `do_sum()` to `float()` calls.
