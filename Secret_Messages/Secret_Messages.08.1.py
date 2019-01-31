"""
Secret_Messages.08.1.py

Decode a secret message given the original and encoded image files.
Use an accumulator class to convert N bit values to text.

Usage: Secret_Messages.08.1.py <original image file> <encoded image file>
"""

import sys
from PIL import Image
import image_iterator
import bitstream_data


# get the original and encoded filenames
if len(sys.argv) != 3:
    print(f'Sorry, expected two filenames')
    sys.exit(1)

original_filename = sys.argv[1]
encoded_filename = sys.argv[2]

print(f'original_filename={original_filename}, encoded_filename={encoded_filename}')

# open input original_filename and get pixel data
original_image = Image.open(original_filename)
(original_image_width, original_image_height) = original_image.size
original_iterator = image_iterator.image_iterator(original_image)

# ditto for the encoded file
encoded_image = Image.open(encoded_filename)
(encoded_image_width, encoded_image_height) = encoded_image.size
encoded_iterator = image_iterator.image_iterator(encoded_image)

# check image sizes - if not the same abort
if (original_image_width != encoded_image_width or
        original_image_height != encoded_image_height):
    print('Sorry, original and encoded images have different sizes.')
    sys.exit(1)

# decode the text message
accum = bitstream_data.DecodeBits(2)
for (o_pix, e_pix) in zip(original_iterator, encoded_iterator):
    # decode this N bit value
    accum.put(o_pix ^ e_pix)

result = accum.get()
print(result)
