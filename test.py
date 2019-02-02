from PIL import Image
from itertools import zip_longest
 
 
def bits_tostring(data):
    result = ''
    accum = 0
    shift = 0
 
    for bits in data:
 
      accum = accum + (bits << shift)
      #print(accum)
      shift += 2
      if shift >= 8:
          result = result + chr(accum)
 
          accum = 0
          shift = 0
     # print(shift)
    return result
 
 
# Now beginning main logic
mode = input("Would you like to [E]ncrypt or [D]ecrypt? \n")
type(mode)
 
if mode == 'E':
 
    image = Image.open('two.bmp')
    pixels = list(image.getdata())
   # print(f'pixels={pixels}')
 
    plaintext = input("What message would you like to hide? \n")
    type(plaintext)
    plaintext_data = plaintext
    new_pixels = []
 
    #The ends of the pixel data contains the least significant bits.
    #By modifying the pixel data with XOR, we modify those bits.
 
    for (pix, ch) in zip(pixels, plaintext_data):
        #print(f'pix={pix}, ch={ch}')
        (r, g, b) = pix
        print(pix)
        new_r = r ^ ord(ch)   # need to convert 'ch' to an integer value
        new_pixels.append((new_r, g, b))
    #print(f'new_pixels={new_pixels}')
 
    image.putdata(new_pixels)
    image.save('two_encoded.bmp')
 
 
if mode == 'D':
 
    image = Image.open('two.bmp')
    pixels = list(image.getdata())
 
    image_encoded = Image.open('two_encoded.bmp')
    pixels_encoded = list(image_encoded.getdata())
 
    decoded_pixels = []
 
    for (pix_plain, pix_encoded) in zip(pixels, pixels_encoded):
        (r_p, g_p, b_p) = pix_plain
        (r_e, g_e, b_e) = pix_encoded
        r_decoded = r_p ^ r_e
        decoded_pixels.append(r_decoded)
    # at this point "decoded_pixels" contains all N bit pixel values for the complete message
    decoded_bits = bits_tostring(decoded_pixels)  # called only once
    print(decoded_bits)
