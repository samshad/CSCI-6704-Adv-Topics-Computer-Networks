def perform_crc_division(bits: list[int], generator: list[int]) -> list[int]:
    """
    Perform the division using the generator polynomial and return the remainder.

    Args:
        bits (list[int]): The input data bits or data with CRC remainder.
        generator (list[int]): The generator polynomial bits.

    Returns:
        list[int]: The remainder after division.
    """
    gen_len = len(generator)
    crc_len = gen_len - 1
    register = [0] * crc_len

    for bit in bits:
        top_bit = register[0]
        register = register[1:] + [bit]
        if top_bit == 1:
            for i in range(crc_len):
                register[i] ^= generator[i + 1]

    return register


def crc(data: str, generator: str) -> tuple[str, str]:
    """
    Calculate the Cyclic Redundancy Check (CRC) for a given data string using a specified generator polynomial.

    Args:
        data (str): The input data string consisting of binary digits (0s and 1s).
        generator (str): The generator polynomial string consisting of binary digits (0s and 1s).

    Returns:
        tuple[str, str]: A tuple containing the transmitted bit string (data + CRC) and the CRC remainder.

    References:
        - Cyclic Redundancy Check in Python: https://www.geeksforgeeks.org/cyclic-redundancy-check-python/
    """

    data_bits = list(map(int, data))
    generator_bits = list(map(int, generator))
    crc_len = len(generator_bits) - 1
    padded_data = data_bits + [0] * crc_len
    remainder_bits = perform_crc_division(padded_data, generator_bits)

    remainder = ''.join(map(str, remainder_bits))
    transmitted_bit_string = ''.join(map(str, data_bits)) + remainder

    return transmitted_bit_string, remainder


def check_crc(data_with_remainder: str, generator: str) -> bool:
    """
    Verify the Cyclic Redundancy Check (CRC) remainder for a given data string using a specified generator polynomial.

    Args:
        data_with_remainder (str): The input data string with appended CRC remainder consisting of binary digits (0s and 1s).
        generator (str): The generator polynomial string consisting of binary digits (0s and 1s).

    Returns:
        bool: True if the CRC check passes (remainder is all zeros), False otherwise.

    References:
        - Cyclic Redundancy Check in Python: https://www.geeksforgeeks.org/cyclic-redundancy-check-python/
    """

    data_with_remainder_bits = list(map(int, data_with_remainder))
    generator_bits = list(map(int, generator))
    remainder_bits = perform_crc_division(data_with_remainder_bits, generator_bits)

    remainder = ''.join(map(str, remainder_bits))
    return remainder == '0' * (len(generator_bits) - 1)
