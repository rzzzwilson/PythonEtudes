from PIL import Image
 
def bits_tostring(data):
    result = ''
    accum = 0
    shift = 0
 
    for bits in data:
      accum = accum + (bits << shift)
      shift += 8
      if shift >= 8:
          result = result + chr(accum)
          accum = 0
          shift = 0
    return result
 
 
# Now beginning main logic
mode = input("Would you like to [E]ncrypt or [D]ecrypt? \n")
mode = mode.upper()     # so user can enter 'e' or 'E', etc
 
if mode == 'E':
    image = Image.open('two.bmp')
    pixels = list(image.getdata())
 
    plaintext = input("What message would you like to hide? \n")
    new_pixels = []
 
    for (pix, ch) in zip(pixels, plaintext):
        (r, g, b) = pix
        new_r = r ^ ord(ch)   # need to convert 'ch' to an integer value
        new_pixels.append((new_r, g, b))
 
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
    decoded_bits = bits_tostring(decoded_pixels)  # called only once
    print(decoded_bits)
