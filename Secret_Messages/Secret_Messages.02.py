"""
Secret_Messages.02.py

Code to return N bit values given a text string.

Usage: Secret_Messages.02.py <number of bits> <text message>
"""
   
# global variables to support "nbit" functions
nbit_data = None
nbit_ch_index = None
nbit_char = None
nbit_index = None
nbit_num_bits = None
nbit_mask = None

def nbits_init(data, num_bits):
    """Initialize the "bit field" routines.

    data      the string of data to form into bit values
    num_bits  the number of bits to return each time
              (must be a power of 2, ie, 1, 2, 4, or 8)
    """

    global bit_data, bit_ch_index, bit_char, bit_index, bit_num_bits, bit_mask

    bit_data = str(data)        # the string to process
    bit_ch_index = 0            # index in string of next character
    bit_char = ord(bit_data[0]) # the current character (as integer)
    bit_index = 8               # index (from right) of next bit field (force next ch)
    bit_num_bits = num_bits     # the number of bits to return
    bit_mask = 2**num_bits - 1  # bit mask for rightmost N bits

def nbits_get():
    """Get the next N bits from the user data string.

    Returns the next N bit field, or None if no data left.
    """

    global bit_ch_index, bit_char, bit_index

    
    # move to next character if we need to
    if bit_index >= 8:
        if bit_ch_index >= len(bit_data):       # if end of text
            return None                         #   return None
        bit_char = ord(bit_data[bit_ch_index])  # else move to next character
        bit_ch_index += 1
        bit_index = 0

    # return next N bits
    result = bit_char & bit_mask                # get low N bits from variable
    bit_char = bit_char >> bit_num_bits         # shift variable to remove bits we are returning
    bit_index += bit_num_bits                   # bump the bit counter
    return result                               # return the result N bits

if __name__ == '__main__':
    import sys

    # get test text and number of bits to return
    if len(sys.argv) != 3:
        print('Usage: Secret_Messages.02.py <number of bits> <text message>')
        sys.exit(1)
    number_of_bits = int(sys.argv[1])
    data = sys.argv[2]
    
    print(f'number_of_bits={number_of_bits}')
    print(f"data='{data}'")
    for ch in data:
        print(f'    {ord(ch):08b}')
    nbits_init(data, number_of_bits)
    while True:
        bits = nbits_get()
        if bits is None:
            break
        print(f'bits={bits:0{number_of_bits}b}')
    
