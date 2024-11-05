"""Md Samshad Rahman"""
"""B00968344"""


def hex_to_binary(hex_string):
    # Reference: https://www.geeksforgeeks.org/python-ways-to-convert-hex-into-binary/

    binary_string = bin(int(hex_string, 16))[2:]
    return binary_string.zfill(4 * len(hex_string))


def bit_stuffing(binary_string):
    # Reference: https://www.geeksforgeeks.org/implementation-of-bit-stuffing-and-bit-destuffing/

    stuffed_string = ""
    consecutive_ones = 0

    for bit in binary_string:
        stuffed_string += bit
        if bit == '1':
            consecutive_ones += 1
            if consecutive_ones == 5:
                stuffed_string += '0'
                consecutive_ones = 0
        else:
            consecutive_ones = 0

    return stuffed_string


def bit_unstuffing(stuffed_string):
    # Reference: https://www.geeksforgeeks.org/implementation-of-bit-stuffing-and-bit-destuffing/

    unstuffed_string = ""
    consecutive_ones = 0

    i = 0
    while i < len(stuffed_string):
        bit = stuffed_string[i]
        unstuffed_string += bit
        if bit == '1':
            consecutive_ones += 1
            if consecutive_ones == 5:
                i += 1
                consecutive_ones = 0
        else:
            consecutive_ones = 0
        i += 1

    return unstuffed_string


def binary_to_hex(binary_string):
    # Reference: https://www.geeksforgeeks.org/python-ways-to-convert-hex-into-binary/

    hex_string = hex(int(binary_string, 2))[2:].upper()
    return hex_string.zfill((len(binary_string) + 3) // 4)


def main():
    hex_string = input("Input: ").upper()

    binary_string = hex_to_binary(hex_string)
    print(f"Conversion to binary: {binary_string}")

    stuffed_binary_string = bit_stuffing(binary_string)
    print(f"After bit stuffing: {stuffed_binary_string}")

    unstuffed_binary_string = bit_unstuffing(stuffed_binary_string)
    print(f"After bit unstuffing: {unstuffed_binary_string}")

    result_hex_string = binary_to_hex(unstuffed_binary_string)
    print(f"Output: {result_hex_string}")


if __name__ == "__main__":
    main()


# Test Cases
# Input: ABEFFFF
# Input: FFFFFFFF
# Input: 7A1
