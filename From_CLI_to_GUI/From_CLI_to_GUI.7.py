"""
Accept two integer numbers from the command line and print the sum.

Usage: From_CLI_to_GUI.7.py <integer> <integer>
"""

import sys

def usage(msg=None):
    """Help the user out.  Also display optional message."""

    if msg:
        print('*' * 60)
        print(msg)
        print('*' * 60)

    print(__doc__)

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
