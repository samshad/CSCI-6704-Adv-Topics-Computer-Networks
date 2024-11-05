from crc_functions import crc, check_crc


def main():
    """
    Main function for CRC calculation and verification.
    """
    print("CRC Calculation and Verification")
    generator = input("Enter the generator polynomial G(x) in binary: ")
    message = input("Enter the message M(x) in binary: ")

    transmitted_message, crc_remainder = crc(message, generator)
    print(f"Transmitted message P(x) (message + CRC): {transmitted_message}")
    print(f"CRC remainder: {crc_remainder}")

    is_valid = check_crc(transmitted_message, generator)
    print(f"CRC verification result: {'valid' if is_valid else 'invalid'}")


if __name__ == "__main__":
    main()
