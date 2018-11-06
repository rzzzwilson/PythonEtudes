"""
Prompt the user for two integer numbers and print the sum.
"""

# get the first integer
while True:
    try:
        int1 = input('Enter the first integer: ')
        int1 = int(int1)    # convert the input string to a number
        break
    except ValueError:
        print(f'Sorry, only want integers.  Something like 123.')

# get the second integer
while True:
    try:
        int2 = input('Enter the second integer: ')
        int2 = int(int2)    # convert the input string to a number
        break
    except ValueError:
        print(f'Sorry, only want integers.  Something like 123.')

# calculate the sum and print it
the_sum = int1 + int2
print(f'The sum of {int1} and {int2} is {the_sum}')
