"""
Secret_Messages.07.0.py

Encode unicode text characters into an image file.

Usage: Secret_Messages.07.0.py <input file> <output file> <number of bits> <text message or file>
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

    nbit_mask = 2**num_bits - 1             # get a "bit mask" with N 1s at the right
    for ch in data:
        for _ in range(8 // num_bits):      # do 8 times for 1 bit, etc
            result.append(ch & nbit_mask)   # get right N bits from character value
            ch >>= num_bits                 # shift to remove right N bits

    return result

def main(input_filename, output_filename, num_bits, text):
    """Encode a text message in an image file.

    input_filename   the name of the input image file
    output_filename  the name of the encoded putput image file
    num_bits         the number of bits to encode with
    text             the text message to encode
    """

    # open input input_filename and get pixel data
    image = Image.open(input_filename)
    (image_width, image_height) = image.size
    num_pixels = image_width * image_height
    max_chars_in_image = num_pixels * 3 * num_bits // 8
    pixels = list(image.getdata())

    # convert the text message in unicode to a sequence of bytes
    text = bytes(text, 'utf-8')

    # ensure the text message isn't too long to be encoded in the image file
    num_chars = len(text)
    if max_chars_in_image < num_chars:
        print(f'Sorry, the image can only contain {max_chars_in_image} characters')
        sys.exit(1)

    # get the text data into a "N bits at a time" list
    nbit_data = string_to_nbits(text, num_bits)

    # convert the flat list of Nbit data into a list of 3-tuples
    temp = []           # place to store partial 3-tuple
    nbit_tuples = []    # the list of 3-tuple Nbit text values
    for val in nbit_data:
        temp.append(val)                    # build temp list
        if len(temp) == 3:                  # if we have 3 elements
            nbit_tuples.append(tuple(temp)) # append tuple to result
            temp = []                       # prepare for next 3
    # handle partial tuple, if any
    if len(temp) > 0:
        while len(temp) < 3:
            temp.append(0)
        nbit_tuples.append(tuple(temp))

    # encode text Nbit values into the image pixel values
    new_pixels = []
    for (nbits, pix) in zip(nbit_tuples, pixels):
        # unpack nbit values and pixel colour values
        (nbit_r, nbit_g, nbit_b) = nbits
        (pix_r, pix_g, pix_b) = pix

        xor_r = pix_r ^ nbit_r
        xor_g = pix_g ^ nbit_g
        xor_b = pix_b ^ nbit_b

        new_pixels.append((xor_r, xor_g, xor_b))    # need to append a tuple

    # update the image and write a new file
    image.putdata(new_pixels)
    image.save(output_filename)


# get the input and output filenames and the text message
if len(sys.argv) != 5:
    print(f'Sorry, expected two filenames, number of bits and a text message')
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]
num_bits = int(sys.argv[3])
text_msg = sys.argv[4]

# maybe 'text_msg' is actually a filename
# try to open the file - if that works read the file contents
# if there is no file then 'text_msg' contains the text to encode
try:
    with open(text_msg) as fd:
        text_msg = fd.read()
except FileNotFoundError:
    pass

print(f'input_filename={input_filename}, output_filename={output_filename}')
print(f'num_bits={num_bits}')
print(f'text_msg:\n{text_msg}')

# call the encode routine
main(input_filename, output_filename, num_bits, text_msg)

