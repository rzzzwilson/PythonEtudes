"""
Secret_Messages.08.1.py

Decode a secret message given the original and encoded image files.
Uses stream data handling.

Usage: Secret_Messages.08.1.py <original image file> <encoded image file>
"""

import sys
from PIL import Image
import image_iterator
import encode_decode


def usage(msg=None):
    """Print usage help, with optional message."""

    if msg:
        print('*' * 60)
        print(msg)
        print('*' * 60)
    print(__doc__)
    print()

def decode(original, encoded):
    """Get an iterator of decoded values.

    original  iterator of original image pixel values
    encoded   iterator of encoded image pixel values

    Returns an iterator of decoded Nbit values.
    """

    for (original, encoded) in zip(original_iterator, encoded_iterator):
        yield original ^ encoded


# get the original and encoded filenames
if len(sys.argv) != 3:
    usage()
    sys.exit(1)

original_filename = sys.argv[1]
encoded_filename = sys.argv[2]

# open the original file and get iterator of the pixel values
original_image = Image.open(original_filename)
original_iterator = image_iterator.image_iterator(original_image)

# open the encoded file and get iterator of the pixel values
encoded_image = Image.open(encoded_filename)
encoded_iterator = image_iterator.image_iterator(encoded_image)

# get the decoded value iterator
decoded_iterator = decode(original_iterator, encoded_iterator)
result = encode_decode.decode(decoded_iterator)
print(result)
