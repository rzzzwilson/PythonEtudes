GUI programming
---------------

Now is the time to look at tkinter "events".  The event we are interested in,
of course, is what happens when the user presses the "+" button.  In tkinter
you can specify the function that runs when the button is pressed when you
create the button, like this::

    self.do_sum = Button(frame, text="+", width=10, command=self.do_sum)

The `command=` keyword parameter to the Button constructor tells tkinter that
when the Button is pressed run the named function.  In this case we run a
function called `self.do_sum()`.  The complete program is::

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

Note that the Button constructor has an extra parameter `width=10` that sets the
width of the button just a bit wider than the default width to make pressing it
easier.  The new program looks like this:

.. image:: From_CLI_to_GUI/From_CLI_to_GUI.9.0.png

We also have to define the `self.do_sum()` function.  The `self` part means it
is a method of the `App` class that defines the GUI application.  In that method
we have to get the text from both Entry widgets, convert the text to integers,
do the addition and display the result.  We choose to print the result to the
console.

Now we test the program by entering the usual test values into the Entry widgets
and pressing the "+" Button::

    $ python3 From_CLI_to_GUI.9.py
    ##### Values "2" and "3" entered
    The sum of 2 and 3 is 5
    ##### Values "2" and "3.0" entered
    Exception in Tkinter callback
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/tkinter/__init__.py", line 1702, in __call__
        return self.func(*args)
      File "From_CLI_to_GUI.9.py", line 27, in do_sum
        int2 = int(int2)
    ValueError: invalid literal for int() with base 10: '3.0'
    ##### Values "2" ONLY entered
    Exception in Tkinter callback
    Traceback (most recent call last):
      File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/tkinter/__init__.py", line 1702, in __call__
        return self.func(*args)
      File "From_CLI_to_GUI.9.py", line 27, in do_sum
        int2 = int(int2)
    ValueError: invalid literal for int() with base 10: ''

We have the expected errors from improper integer strings plus an error because
didn't put any text into an Entry widget.

On the
`next page <https://github.com/rzzzwilson/PythonEtudes/wiki/From_CLI_to_GUI.10>`_
we handle the errors in a way that should be becoming familiar to you.
