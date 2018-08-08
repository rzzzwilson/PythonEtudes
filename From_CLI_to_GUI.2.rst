Checking our code
-----------------

Part of writing a sturdy code solution is to test the code.  It's amazing
how often a solution that works actually has many bugs still in it!

Testing
-------

We saw on the previous page that adding `2` and `3` worked.  Let's try something
different::

    $ python3 From_CLI_to_GUI.1.py
    Enter the first integer: 2
    Enter the second integer: 3.0      # note, a floating point number!
    Traceback (most recent call last):
      File "From_CLI_to_GUI.1.py", line 8, in <module>
        int2 = int(int2)
    ValueError: invalid literal for int() with base 10: '3.0'

Testing has two parts::

- testing what the code does for correct inputs, and
- testing what the code does for incorrect inputs.

The test above showed that our solution crashed when one of the input values
was a floating point number.  The exception occurred when we tried to convert
the string containing "3.0" into an integer.

Here's another test run::

    $ python3 From_CLI_to_GUI.1.py
    Enter the first integer: 2
    Enter the second integer: three
    Traceback (most recent call last):
      File "From_CLI_to_GUI.1.py", line 8, in <module>
        int2 = int(int2)
    ValueError: invalid literal for int() with base 10: 'three'

Now when one of the inputs isn't an integer or float we get a similar error.

Handling user input
-------------------

It's tempting to say "well, that's the user's problem, we did ask for integers",
but when you write software for people to use it's nice to not just crash when
the user inputs something unacceptable.  It's far better to point out their
error, give them a little direction and ask them to try again.  One way of doing
this in python is something like this (we handle just one number in this
code fragment)::

    while True:
        try:
            int1 = input('Enter the first integer: ')
            int1 = int(int1)    # convert the input string to a number
            break
        except ValueError:
            print(f'Sorry, only want integers.  Something like 123.')

Since we may ask the user to try a multiple number of times we use a while loop.
This means we'll ask the user again and again until we break out of the loop.
Putting that new code into our program for both input numbers, we get::

    """
    Prompt the user for two integer numbers and print the sum.
    """

    while True:
        try:
            int1 = input('Enter the first integer: ')
            int1 = int(int1)    # convert the input string to a number
            break
        except ValueError:
            print(f'Sorry, only want integers.  Something like 123.')

    while True:
        try:
            int2 = input('Enter the second integer: ')
            int2 = int(int2)    # convert the input string to a number
            break
        except ValueError:
            print(f'Sorry, only want integers.  Something like 123.')

    the_sum = int1 + int2
    print(f'The sum of {int1} and {int2} is {the_sum}')

Now when we repeat the testing from the last page, we see::

    $ python3 From_CLI_to_GUI.2.py
    Enter the first integer: 2
    Enter the second integer: 3.0
    Sorry, only want integers.  Something like 123.
    Enter the second integer: three
    Sorry, only want integers.  Something like 123.
    Enter the second integer: 3
    The sum of 2 and 3 is 5

So far so good.  But now we can refactor a little on the
`next page <https://github.com/rzzzwilson/PythonEtudes/wiki/From_CLI_to_GUI.3>`_.
        
