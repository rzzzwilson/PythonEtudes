"""
Secret_Messages.02.py

Code to return N bit values given a text string.

Usage: Secret_Messages.02.py <number of bits> <text message>
"""

def string_to_nbits(data, num_bits):
    """Convert a sequence of 8 bit characters into a list of N bit values.

    data      a sequence of 8 bit characters
    num_bits  the number of bits in the N bit values

    Returns a list of the N bit values.
    """

    result = []

    nbit_mask = 2**num_bits - 1                 # get a "bit mask" with N 1s at the right
    for ch in data:
        ch_value = ord(ch)                      # convert character to a decimal value
        for _ in range(8 // num_bits):          # do 8 times for 1 bit, etc
            result.append(ch_value & nbit_mask) # get right N bits from character value
            ch_value >>= num_bits               # shift to remove right N bits

    return result

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
        print(f"    {ord(ch):08b} = '{ch}'")
    nbits_list = string_to_nbits(data, number_of_bits)
    for nbit_value in nbits_list:
        print(f'nbit_value={nbit_value:0{number_of_bits}b}')
    
