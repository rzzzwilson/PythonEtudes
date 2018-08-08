Error checking
--------------

We noticed that passing incorrect parameters to the CLI program resulted in
`ValueError` exceptions, similar to those from the original program when the
user entered "3.0" and "three" at the prompt.  The error checking code used
to nicely catch those errors will also work here.  But getting parameters
from `sys.argv` opens the possibility of a different sort of error - what
happens if the user doesn't give us enough parameters?

::

    $ python3 From_CLI_to_GUI.5.py 2
    Traceback (most recent call last):
      File "From_CLI_to_GUI.5.py", line 9, in <module>
        int2 = int(sys.argv[2])
    IndexError: list index out of range

We get an `IndexError` exception caused by trying to access an element that
isn't in the list.  We can get a better understanding by again running the
little `sys.argv.py` program with the same parameters::

    $ python3 sys.argv.py 2
    ['sys.argv.py', '2']

Only two elements in the list!  How can we check if the user gave us the right
number of parameters?  `sys.argv` is just a python list, and we can check the
length of a list with the
`len() function <https://docs.python.org/3/library/functions.html#len>`_.
We also add a helper function to check that the parameters given can be
converted to an integer::

    """
    Accept two integer numbers from the command line and print the sum.
    """

    import sys

    def ensure_int(int_str):
        """Convert a string to an integer and return the integer value"""

        try:
            int_value = int(int_str)
            return int_value
        except ValueError:
            print(f'Sorry, only want integers.  Something like 123.')
            sys.exit(1)

    # check that we have the right number of parameters
    if len(sys.argv) != 3:
        print('Wrong number of parameters!')
        sys.exit(1)

    # get the numbers from the command line sys.argv
    int1 = ensure_int(sys.argv[1])
    int2 = ensure_int(sys.argv[2])
    the_sum = int1 + int2
    print(f'The sum of {int1} and {int2} is {the_sum}')

Note that even though we want two parameter numbers we check to make sure that
`sys.argv` has length 3 because the list also includes the script name at
index 0.  Also note that we check that `sys.argv` has exactly **three**
elements, not just three or more.  If the user supplies more numbers than we can
use our code won't crash, but it's better that the user uses our code properly.
It is better to limit the user like this because it's possible that we want to
allow extra parameters later on and if the user has been using extra parameters
that didn't raise an error, her code that used to work will suddenly get errors
because we changed the way our code worked.

Now when we test our code with varying numbers of parameters we see::

    $ python3 From_CLI_to_GUI.5.py 2
    Wrong number of parameters!
    $ python3 From_CLI_to_GUI.5.py 2 3
    The sum of 2 and 3 is 5
    $ python3 From_CLI_to_GUI.5.py 2 3.0
    Sorry, only want integers.  Something like 123.
    $ python3 From_CLI_to_GUI.5.py 2 three
    Sorry, only want integers.  Something like 123.
    $ python3 From_CLI_to_GUI.5.py 2 3 4
    Wrong number of parameters!

On the 
`next page <https://github.com/rzzzwilson/PythonEtudes/wiki/From_CLI_to_GUI.6>`_
we will give the user better help when they make an error using our application.

