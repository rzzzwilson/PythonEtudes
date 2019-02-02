"""
Secret_Messages.08.py

Encode unicode text characters into an image file.
This version uses iterators for text and image data.

Usage: Secret_Messages.08.py <input file> <output file> <text message or file>
"""

import sys
from PIL import Image
import image_iterator
import encode_decode

# default values
BitsPerPixelColour = 2      # 2 bits per colour value
NumPixelColourValues = 4    # using 4 pixel values, RGBA
BitsPerColour = 8           # 8 bits per colour value


def main(input_filename, output_filename, text):
    """Encode a text message in an image file.

    input_filename   the name of the input image file
    output_filename  the name of the encoded putput image file
    text             the text message to encode

    The text data is encoded 'BitsPerPixelColour' bits at a time into each of
    the pixel colour values.
    """

    # open input input_filename and get pixel data
    image = Image.open(input_filename)
    (image_width, image_height) = image.size
    num_pixels = image_width * image_height
    pixels = list(image.getdata())

    # convert the text message in unicode to a sequence of bytes
    byte_text = bytes(text, 'utf-8')

    # ensure the image is big enough to encode the message
    num_encode_values = 8 + 8*4//BitsPerPixelColour + len(byte_text)*8//BitsPerPixelColour
    if num_encode_values > num_pixels * NumPixelColourValues:
        print(f"Sorry, the image can't hold a message that long.")
        sys.exit(1)

    # prepare the image pixel value iterator
    image_pix = image_iterator.image_iterator(image, num_pixels)

    # get the N bit stream of data to encode
    data_stream = encode_decode.encode_string(text, BitsPerPixelColour)

    # encode each message into the image pixel values
    new_pixels_list = []
    new_pix = []
    for (pix, nbits) in zip(image_pix, data_stream):
        print(f'nbits={nbits:0{BitsPerPixelColour}b}')
        new_pix.append(pix ^ nbits)
        if len(new_pix) == NumPixelColourValues:
            new_pixels_list.append(tuple(new_pix))    # need to append a tuple
            new_pix = []

    # update the image and write a new file
    image.putdata(new_pixels_list)
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

# call the encode routine
main(input_filename, output_filename, text_msg)

