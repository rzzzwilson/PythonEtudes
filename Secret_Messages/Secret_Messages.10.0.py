"""
Secret_Messages.10.0.py

Encode unicode text characters into an image file.
This version uses iterators for text and image data.

Usage: Secret_Messages.10.0.py <input file> <output file> <number of bits> <text message or file>
"""

import sys
from PIL import Image
import image_iterator
import encode_decode

# we assume that all pixels have three band values
NumPixelColourValues = 3


def main(input_filename, output_filename, num_bits, text):
    """Encode a text message in an image file.

    input_filename   the name of the input image file
    output_filename  the name of the encoded putput image file
    num_bits         the number of bits to encode the message with
    text             the text message to encode

    The text data is encoded 'num_bits' bits at a time into each of
    the pixel colour values.
    """

    # open input input_filename and get pixel data
    image = Image.open(input_filename)
    (image_width, image_height) = image.size
    num_pixels = image_width * image_height
    pixels = list(image.getdata())
    if len(pixels[0]) != NumPixelColourValues:
        print(f'Sorry, image has {len(pixels[0])} bands, can only handle {NumPixelColourValues}.')
        sys.exit(1)

    # ensure the image is big enough to encode the message
    encode_size = encode_decode.encode_size(text, num_bits)
    if encode_size > num_pixels * NumPixelColourValues:
        print(f"Sorry, the image can't hold a message that long.")
        sys.exit(1)

    # prepare the image pixel value iterator
    image_pix = image_iterator.image_iterator(image)

    # get the N bit stream of data to encode
    data_stream = encode_decode.encode(text, num_bits)

    # encode the message into the image pixel values
    new_pixels_list = []
    new_pix = []
    for (pix, nbits) in zip(image_pix, data_stream):
        new_pix.append(pix ^ nbits)
        if len(new_pix) == NumPixelColourValues:
            new_pixels_list.append(tuple(new_pix))    # need to append a tuple
            new_pix = []

    # flush 'new_pix' if it has data
    if new_pix:
        # while 'new_pix' isn't full append original pix data
        while len(new_pix) < NumPixelColourValues:
            new_pix.append(next(image_pix))
        new_pixels_list.append(tuple(new_pix))

    # update the image and write a new file
    image.putdata(new_pixels_list)
    image.save(output_filename)

def usage(msg=None):
    if msg:
        print('8' * 60)
        print(msg)
        print('8' * 60)
    print(__doc__)
    print()

# get the input and output filenames and the text message
if len(sys.argv) != 5:
    usage()
    sys.exit(1)

input_filename = sys.argv[1]
output_filename = sys.argv[2]
num_bits = sys.argv[3]
text_msg = sys.argv[4]

# check that 'num_bits' is a valid integer
try:
    num_bits = int(num_bits)
except ValueError:
    print(f"Sorry, 'num_bits' isn't a valid integer.")
    sys.exit(1)
if num_bits not in (1, 2, 4, 8):
    print(f"Sorry, 'num_bits' must be 1, 2, 4 or 8.  Got '{num_bits}'")
    sys.exit(1)

# maybe 'text_msg' is actually a filename
# try to open the file - if that works read the file contents
# if there is no file then 'text_msg' contains the text to encode
try:
    with open(text_msg) as fd:
        text_msg = fd.read()
except FileNotFoundError:
    pass

# call the image encode routine
main(input_filename, output_filename, num_bits, text_msg)

