Introduction
============

This etude will discuss adding two numbers together.  We are not really
interested in how you add two numbers in python, as that's boring::

    s = 1 + 2

What we are interested in here is how you approach adding two numbers
starting with a very simple command line (CLI) program with nothing in
the way of error checking.  At each new stage we will add some desirable
feature such as error checking and produce a better body of code.

Problem Description
-------------------

Write a command line program that will ask the user for two integer numbers
and print the sum of those two numbers before finishing.

The code
--------

The simplest program imaginable would look like this::

    """
    Prompt the user for two integer numbers and print the sum.
    """
    
    int1 = input('Enter the first integer: ')
    int2 = input('Enter the second integer: ')
    the_sum = int1 + int2
    print(f'The sum of {int1} and {int2} is {the_sum}')

However, when we run this program, we see::

    $ python3 From_CLI_to_GUI.0.py
    Enter the first integer: 2
    Enter the second integer: 3
    The sum of 2 and 3 is 23

So we see there is a problem.  The sum of **2** and **3** should be **5**,
but we get **23**!?  This is a very common beginner mistake, and is caused
because the `input()` function always returns a string.  We have to convert
the user input strings into integer values before attempting the integer 
addition.

Why did we get the **23** result?  That happens because we tried to add two
strings and, as it happens, the `+` operator is overloaded for strings and
results in string concatenation.

On to the
`next attempt <https://github.com/rzzzwilson/PythonEtudes/wiki/From_CLI_to_GUI.1>`_.
    
