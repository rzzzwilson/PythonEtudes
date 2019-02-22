"""
Secret_Messages.06.py

Decode a secret message given the original and encoded image files.

Usage: Secret_Messages.06.py <original image file> <encoded image file>
"""

import sys
from PIL import Image

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

# get the original and encoded filenames
if len(sys.argv) != 3:
    print(f'Sorry, expected two filenames')
    sys.exit(1)

original_filename = sys.argv[1]
encoded_filename = sys.argv[2]

print(f'original_filename={original_filename}, encoded_filename={encoded_filename}')

# open input original_filename and get pixel data
original_image = Image.open(original_filename)
original_pixels = list(original_image.getdata())

# ditto for the encoded file
encoded_image = Image.open(encoded_filename)
encoded_pixels = list(encoded_image.getdata())

# decode the text message
bits_init_tostring(2)
for (o_pix, e_pix) in zip(original_pixels, encoded_pixels):
    # unpack each pixel tuple
    (o_r, o_g, o_b) = o_pix
    (e_r, e_g, e_b) = e_pix

    # decode the three pixel values
    bits_r = o_r ^ e_r
    bits_put_tostring(bits_r)
    bits_g = o_g ^ e_g
    bits_put_tostring(bits_g)
    bits_b = o_b ^ e_b
    bits_put_tostring(bits_b)

print(bits_init_tostring(2))
