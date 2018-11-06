"""
Accept two integer numbers from the command line and print the sum.
"""

import sys

# get the numbers from the command line sys.argv
int1 = int(sys.argv[1])
int2 = int(sys.argv[2])
the_sum = int1 + int2
print(f'The sum of {int1} and {int2} is {the_sum}')
