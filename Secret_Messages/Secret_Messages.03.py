"""
Secret_Messages.03.py

Encode text characters into an image file.

Usage: Secret_Messages.03.py <input file> <output file> <text message>
"""

import sys
from PIL import Image


def string_to_nbits(data, num_bits):
    """Convert a sequence of 8 bit characters into a list of N bit values.

    data      a sequence of 8 bit characters
    num_bits  the number of bits in the N bit values

    Returns a list of the N bit values.
    """

    result = []

    nbit_mask = 2**num_bits - 1                 # get a "bit mask" with N 1s at the right
    for ch in data:
        ch_value = ord(ch)                      # convert character to a decimal value
        for _ in range(8 // num_bits):          # do 8 times for 1 bit, etc
            result.append(ch_value & nbit_mask) # get right N bits from character value
            ch_value >>= num_bits               # shift to remove right N bits

    return result

def main(input_filename, output_filename, text):
    """Encode a text message in all colours of an image file.

    input_filename   the name of the input image file
    output_filename  the name of the encoded putput image file
    text             the text message to encode

    The text data is encoded 2 bits at a time into each of the three pixel
    colour values.
    """

    num_bits = 2

    # open input input_filename and get pixel data
    image = Image.open(input_filename)
    (image_width, image_height) = image.size
    num_pixels = image_width * image_height
    max_chars_in_image = num_pixels * 3 * num_bits // 8
    pixels = image.getdata()

    # ensure the text message isn't too long to be encoded in the image file
    num_chars = len(text)
    if max_chars_in_image < num_chars:
        print(f'Sorry, the image can only contain {max_chars_in_image} characters')
        sys.exit(1)

    # get the text data into a "2 bits at a time" list
    nbit_data = string_to_nbits(text, num_bits)

    # convert the flat list of Nbit data into a list of 3-tuples
    temp = []           # place to store partial 3-tuple
    nbit_tuples = []    # the list of 3-tuple Nbit text values
    for val in nbit_data:
        temp.append(val)                    # build temp list
        if len(temp) == 3:                  # if we have 3 elements
            nbit_tuples.append(tuple(temp)) # append tuple to result
            temp = []                       # prepare for next 3
    # handle partial "temp", if any
    if len(temp) > 0:
        while len(temp) < 3:
            temp.append(0)
        nbit_tuples.append(tuple(temp))

    # encode text Nbit values into the image pixel values
    new_pixels = []
    for (nbits, pix) in zip(nbit_tuples, pixels):
        # unpack nbit values and pixel colour values
        (e_r, e_g, e_b) = nbits
        (r, g, b) = pix

        xor_r = r ^ e_r
        xor_g = g ^ e_g
        xor_b = b ^ e_g

        new_pixels.append((xor_r, xor_g, xor_b))    # need to append a tuple

    # update the image and write a new file
    image.putdata(new_pixels)
    image.save(output_filename)


# get the input and output filenames and the text message
if len(sys.argv) != 4:
    print(f'Sorry, expected two filenames and a text message')
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]
text_msg = sys.argv[3]

print(f'input_filename={input_filename}, output_filename={output_filename}, text_msg={text_msg}')

main(input_filename, output_filename, text_msg)

