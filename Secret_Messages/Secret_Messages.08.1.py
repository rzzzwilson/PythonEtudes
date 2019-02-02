"""
Secret_Messages.08.1.py

Decode a secret message given the original and encoded image files.
Use an accumulator class to convert N bit values to text.

Usage: Secret_Messages.08.1.py <encoded image file>
"""

import sys
from PIL import Image
import image_iterator
import encode_decode


# get the encoded filename
if len(sys.argv) != 2:
    print(f'Sorry, expected a filename')
    sys.exit(1)

encoded_filename = sys.argv[1]

# open the encoded file and get iterator of the pixel values
encoded_image = Image.open(encoded_filename)
encoded_iterator = image_iterator.image_iterator(encoded_image)

result = encode_decode.decode_data(list(encoded_iterator))
print(result)
