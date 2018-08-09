GUI programming
---------------

The previous program just printed the results and errors to the console.  This
is not good practice because GUI programs are often run from the desktop where
there *is* no console.  All GUI systems have a method of displaying text in a
graphical way.  Tkinter has the
`messagebox <https://pythonspot.com/tk-message-box/>`_ dialog for this.

In this program we don't "wild card" import from `tkinter`.
This is bad practice because it fills the namespace of the application with
all the tkinter names which could clash with the names we use ourselves.  It's
better to specifically import what we need, like this::

    from tkinter import Tk, Frame, Entry, Button, LEFT, messagebox

Here's the program::

    """
    Display the sum of two integers when a button is pressed.

    Usage: From_CLI_to_GUI.8.py
    """

    from tkinter import Tk, Frame, Entry, Button, LEFT, messagebox

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
            int1 = self.integer1.get()
            int1 = self.str_to_int(int1)
            int2 = self.integer2.get()
            int2 = self.str_to_int(int2)
            if int1 is None or int2 is None:
                self.error('Sorry, need two integer strings.')
            else:
                the_sum = int1 + int2
                self.info(f'The sum of {int1} and {int2} is {the_sum}')

        def str_to_int(self, value):
            """Get an integer from a string.  Return None if can't get integer."""

            try:
                result = int(value)
                return result
            except ValueError:
                return None

        def info(self, msg):
            """Display an information message."""

            messagebox.showinfo("Info", msg)

        def error(self, msg):
            """Display an error message."""

            messagebox.showerror("Error", msg)

    root = Tk()
    app = App(root)
    root.mainloop()

The two new methods `info()` and `error()` display information and error
messages, respectively.  When we conduct tests on the new program we see the
normal result dialog and the error dialogs resulting from various inputs.

Normal result:

.. image:: From_CLI_to_GUI/From_CLI_to_GUI.11.0.png

Error due to a bad integer string:

.. image:: From_CLI_to_GUI/From_CLI_to_GUI.11.1.png

Error due to a missing integer string:

.. image:: From_CLI_to_GUI/From_CLI_to_GUI.11.2.png

On the 
`next page <https://github.com/rzzzwilson/PythonEtudes/wiki/From_CLI_to_GUI.12>`_
we discuss and implement methods of presenting a better GUI to the user.
