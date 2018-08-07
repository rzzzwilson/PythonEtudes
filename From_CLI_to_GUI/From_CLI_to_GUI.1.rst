Converting a string to an integer
---------------------------------

The `int() function <https://docs.python.org/3/library/functions.html#int>`_
converts a string to an integer.  We modify our code to be::

    """
    Prompt the user for two integer numbers and print the sum.
    """

    int1 = input('Enter the first integer: ')
    int1 = int(int1)    # convert the input string to a number
    int2 = input('Enter the second integer: ')
    int2 = int(int2)
    the_sum = int1 + int2
    print(f'The sum of {int1} and {int2} is {the_sum}')

Now when we run with the previous input values we see::

    $ python3 From_CLI_to_GUI.1.py
    Enter the first integer: 2
    Enter the second integer: 3
    The sum of 2 and 3 is 5

That looks better!  Are we finished?

Find out on the
`next page <https://github.com/rzzzwilson/PythonEtudes/wiki/From_CLI_to_GUI/From_CLI_to_GUI.2>`_.
    
