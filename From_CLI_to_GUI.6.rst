Helping the user
----------------

The previous program printed short messages when the user entered incorrect
parameters.  For this little etude that's probably good enough.  But when a
program has a more complicated set of parameters it's better to give the user
more help.

Traditionally, in the UNIX world, there was a "man" page for every command in
the operating system.
`Here's one <http://linuxcommand.org/lc3_man_pages/cdh.html>`_ for the `cd`
command.  This idea was carried over into all command line programs written by
users, though this "usage" information was shorter.

We will add this idea to our program.  Because we have more than one place in
our code where we report a user error it makes sense that this extra code is
put into a function which we will call `usage()`::

    """
    Accept two integer numbers from the command line and print the sum.
    """

    import sys

    def usage(msg=None):
        """Help the user out.  Also display optional message."""

        if msg:
            print('*' * 60)
            print(msg)
            print('*' * 60)
            print('')

        print('This is a program to convert a string to an integer and return the integer value.')
        print('')
        print('Usage: From_CLI_to_GUI.6.py <integer> <integer>')
        print('')

    def ensure_int(int_str):
        """Convert a string to an integer and return the integer value"""

        try:
            int_value = int(int_str)
            return int_value
        except ValueError:
            usage('Sorry, only want integers.  Something like 123.')
            sys.exit(1)

    # check that we have the right number of parameters
    if len(sys.argv) != 3:
        usage('Wrong number of parameters!')
        sys.exit(1)

    # get the numbers from the command line sys.argv
    int1 = ensure_int(sys.argv[1])
    int2 = ensure_int(sys.argv[2])
    the_sum = int1 + int2
    print(f'The sum of {int1} and {int2} is {the_sum}')

When we test our code we see::

    $ python3 From_CLI_to_GUI.6.py 2
    ************************************************************
    Wrong number of parameters!
    ************************************************************
    
    This is a program to convert a string to an integer and return the integer value.
    
    Usage: From_CLI_to_GUI.6.py <integer> <integer>
    
    $ python3 From_CLI_to_GUI.6.py 2 3
    The sum of 2 and 3 is 5
    $ python3 From_CLI_to_GUI.6.py 2 3.0
    ************************************************************
    Sorry, only want integers.  Something like 123.
    ************************************************************
    
    This is a program to convert a string to an integer and return the integer value.
    
    Usage: From_CLI_to_GUI.6.py <integer> <integer>
    
    $ python3 From_CLI_to_GUI.6.py 2 3 4
    ************************************************************
    Wrong number of parameters!
    ************************************************************
    
    This is a program to convert a string to an integer and return the integer value.
    
    Usage: From_CLI_to_GUI.6.py <integer> <integer>

On the
`next page <https://github.com/rzzzwilson/PythonEtudes/wiki/From_CLI_to_GUI.7>`_
we will make this `usage()` function  little more general.

