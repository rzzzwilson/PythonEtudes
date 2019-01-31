"""
Secret_Messages.08.py

Encode unicode text characters into an image file.

Usage: Secret_Messages.08.py <input file> <output file> <text message or file>
"""

import sys
from PIL import Image
import data_bitstream
import bitstream_data


def main(input_filename, output_filename, text):
    """Encode a text message in an image file.

    input_filename   the name of the input image file
    output_filename  the name of the encoded putput image file
    text             the text message to encode

    The text data is encoded 2 bits at a time into each of the three pixel
    colour values.
    """

    # open input input_filename and get pixel data
    image = Image.open(input_filename)
    (image_width, image_height) = image.size
    num_pixels = image_width * image_height
    max_chars_in_image = num_pixels * 3 * 2 // 8
    pixels = list(image.getdata())

    # convert the text message in unicode to a sequence of bytes
    text = bytes(text, 'utf-8')

    # ensure the text message isn't too long to be encoded in the image file
    num_chars = len(text)
    if max_chars_in_image < num_chars:
        print(f'Sorry, the image can only contain {max_chars_in_image} characters')
        sys.exit(1)

    # prepare the text message "N bits at a time" software
    data_bits = Bi(text, 2)

    # encode each N bits into the image pixel values
    new_pixels = []
    for pix in pixels:
        # get pixel colour values, handle a fourth value
        if len(pix) == 3:
            (r, g, b) = pix
            a = 255
        if len(pix) == 4:
            (r, g, b, a) = pix

        nbits = nbits_get()     # get N bits
        if nbits is None:       # if None
            break               #     break out of encode, we're done
        xor_r = r ^ nbits

        nbits = nbits_get()
        if nbits is None:
            nbits = 0
        xor_g = g ^ nbits

        nbits = nbits_get()
        if nbits is None:
            nbits = 0
        xor_b = b ^ nbits

        new_pixels.append((xor_r, xor_g, xor_b, a))    # need to append a tuple

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

# maybe 'text_msg' is actually a filename
# try to open the file - if that works read the file contents
# if there is no file then 'text_msg' contains the text to encode
try:
    with open(text_msg) as fd:
        text_msg = fd.read()
except FileNotFoundError:
    pass

print(f'input_filename={input_filename}, output_filename={output_filename}')
print(f'text_msg:\n{text_msg}')

# call the encode routine
main(input_filename, output_filename, text_msg)

