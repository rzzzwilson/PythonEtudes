Command line parameters
-----------------------

We would now like our program to accept the two numbers from the command line
like this::

    $ python3 From_CLI_to_GUI.4.py 2 3
    The sum of 2 and 3 is 5

We can do this using a list called
`sys.argv <https://docs.python.org/3/library/sys.html#sys.argv>`_.  If we write
this little bit of python in a file called `sys.argv.py` and execute it,xi
we see::

    import sys
    print(sys.argv)

    $ python3 sys.argv.py 2 3
    ['sys.argv.py', '2', '3']

Note that `sys.argv` is just a regular python list and contains the number `2`
and `3` that we typed in, along with the name of the script executed as the 
first element of the list.  Your python code can read the `2` and `3` values
from the list.  Note that all the elements of `sys.argv` are strings.

So the code for this program is::

    """
    Accept two integer numbers from the command line and print the sum.
    """

    import sys

    # get the numbers from the command line sys.argv
    int1 = int(sys.argv[1])
    int2 = int(sys.argv[2])
    the_sum = int1 + int2
    print(f'The sum of {int1} and {int2} is {the_sum}')

Testing
-------

As always, we test our code::

    $ python3 From_CLI_to_GUI.4.py 2 3
    The sum of 2 and 3 is 5

    $ python3 From_CLI_to_GUI.4.py 2 3.0
    Traceback (most recent call last):
      File "From_CLI_to_GUI.4.py", line 9, in <module>
        int2 = int(sys.argv[2])
    ValueError: invalid literal for int() with base 10: '3.0'

    $ python3 From_CLI_to_GUI.4.py 2 three
    Traceback (most recent call last):
      File "From_CLI_to_GUI.4.py", line 9, in <module>
        int2 = int(sys.argv[2])
    ValueError: invalid literal for int() with base 10: 'three'

The program works well for the standard test, but fails with exceptions when
we don't provide integer strings.  We expected this because our code doesn't
have any code to handle errors.  We'll do that on the 
`next page <https://github.com/rzzzwilson/PythonEtudes/wiki/From_CLI_to_GUI.5>`_.
