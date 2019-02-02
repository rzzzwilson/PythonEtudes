"""
A generator function returning N bits at a time of a string.
"""

def stream(data, num_bits):
        """Initialize the bit_stream() generator.

        data      the string to stream as N bits at a time
        num_bits  the number of bits to stream (1, 2, 4 or 8)

        Generates a stream of N bit values from the string.
        """

        # check the number of bits to stream and create the bit mask
        if num_bits not in [1, 2, 4, 8]:
            raise ValueError(f"Bad value for 'num_bits', got {num_bits}, "
                              "expected one of 1, 2, 4 or 8.")
        mask = 2**num_bits - 1      # bit mask for rightmost N bits

        bit_data = bytes(data)

        for ch in bit_data:
            count = 0
            while count < 8:
                yield ch & mask         # yield low N bits from variable
                ch = ch >> num_bits     # shift variable to remove bits we are returning
                count += num_bits       # bump the bit counter
            

if __name__ == '__main__':
    import sys

    # get test text and number of bits to return
    if len(sys.argv) != 3:
        print('Usage: xyzzy.py <number of bits> <text message>')
        sys.exit(1)
    number_of_bits = int(sys.argv[1])
    data = sys.argv[2]

    print(f'number_of_bits={number_of_bits}')
    print(f"data='{data}'")
    for ch in data:
        print(f'    {ord(ch):08b}')
    for bits in bit_stream(data, number_of_bits):
        print(f'bits={bits:0{number_of_bits}b}')

