"""
Secret_Messages.05.py

Decode a list of N bit values into a text string.

Usage: Secret_Messages.05.py
"""

number_of_bits = 0      # the number of bits in each value (ie, N)
accum = 0               # accumulator for N bit values
shift = 0               # counter of how far to shift left
result = ''             # place to save each decoded character

def bits_init_tostring(numbits):
    """Initialize the decode system.

    numbits  the number of bits in each decode value (1, 2, 4 or 8)

    Returns the previous decoded string, if any.
    """

    global number_of_bits, accum, shift, result

    old_result = result

    number_of_bits = numbits    # remember the bit value size (ie, N)
    accum = 0
    shift = 0
    result = ''

    return old_result           # return the previous string

def bits_put_tostring(bits):
    """Accumulate an N bit value.

    bits  the N bit value to accumulate
    """

    global accum, shift, result

    accum += bits << shift
    shift += number_of_bits
    if shift >= 8:
        result += chr(accum)
        accum = 0
        shift = 0

# test code
data = [1, 2, 0, 1, 0, 1, 3, 1,    # the 2bit-encoded message
        0, 0, 2, 0, 3, 1, 3, 1,
        3, 3, 2, 1, 2, 0, 3, 1,
        3, 2, 2, 1, 3, 0, 3, 1,
        1, 0, 2, 0]

bits_init_tostring(2)
for val in data:
    bits_put_tostring(val)
print(bits_init_tostring(2))
