Refactoring
-----------

Our solution works well so far, but we have a lot of duplicated code.  It's
often a good idea to remove duplicated code, replacing it with a function.
We call this `refactoring <https://en.wikipedia.org/wiki/Code_refactoring>`_.

This is our duplicated code::

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

Note that the two bits of code are identical except for the prompt strings and
the variables used to hold the resultant integer.  We can write a function that
does what one piece of code does.  We handle the prompt string difference by
passing that into the function when we call it.  The resultant integer is
returned by the function and placed into a variable of our choice.

So now our code looks like this::

    """
    Prompt the user for two integer numbers and print the sum.
    """

    def get_integer(prompt):
        """Prompt the user and return only an integer value."""

        while True:
            try:
                int_value = input(prompt)
                int_value = int(int_value)
                return int_value
            except ValueError:
                print(f'Sorry, only want integers.  Something like 123.')

    int1 = get_integer('Enter the first integer: ')
    int2 = get_integer('Enter the second integer: ')
    the_sum = int1 + int2
    print(f'The sum of {int1} and {int2} is {the_sum}')

Note that even though we added the new function the number of lines of code
decreased from the previous version.  That's not *always* true and it's
actually unimportant.  The real win from this change is that we have simplified
the top-level code::

    int1 = get_integer('Enter the first integer: ')
    int2 = get_integer('Enter the second integer: ')
    the_sum = int1 + int2
    print(f'The sum of {int1} and {int2} is {the_sum}')

Before, all that *while* loop code distracted us from seeing what was actually
happening at a logical level.  We now have a function **get_integer()** that,
once we have figured out what it does, we can **forget about** the details of
how it works because that isn't important at the top-level.  We have actually
simplified the logic of the program.

This abstraction and hiding of complexity is one of your most powerful tools.
You should always be on the lookout for duplicated code and try to refactor the
duplication.

Testing
-------

Repeating the simple test shows that the code behaves axactly as before::

    $ python3 From_CLI_to_GUI.3.py
    Enter the first integer: 2
    Enter the second integer: 3.0
    Sorry, only want integers.  Something like 123.
    Enter the second integer: three
    Sorry, only want integers.  Something like 123.
    Enter the second integer: 3
    The sum of 2 and 3 is 5

Good.  But now we would like to write a version that takes the numbers from the
command line, like this::

    $ python3 From_CLI_to_GUI.4.py 2 3
    The sum of 2 and 3 is 5

Look on the
`next page <https://github.com/rzzzwilson/PythonEtudes/wiki/From_CLI_to_GUI/From_CLI_to_GUI.4>`_
for the solution.
        
