import random
import pandas as pd
from crc_functions import crc, check_crc


def generate_random_binary_string(length: int) -> str:
    """
    Generate a random binary string of a given length.

    Args:
        length (int): The length of the binary string to generate.

    Returns:
        str: A random binary string of the specified length.
    """
    return ''.join(random.choice('01') for _ in range(length))


def introduce_burst_error(data: str, burst_length: int) -> str:
    """
    Introduce a burst error of a specified length into a binary string.

    Args:
        data (str): The original binary string.
        burst_length (int): The length of the burst error to introduce.

    Returns:
        str: The binary string with the burst error introduced.
    """
    error_position = random.randint(0, len(data) - burst_length)
    burst_error = ''.join('1' if bit == '0' else '0' for bit in data[error_position:error_position + burst_length])
    return data[:error_position] + burst_error + data[error_position + burst_length:]


def main():
    """
    Main function to conduct CRC error detection experiments with burst errors.

    This function generates a random binary string, calculates the CRC remainder,
    introduces burst errors, and checks for error detection. The results are stored
    in a DataFrame and written to a CSV file.

    Args:
        None

    Returns:
        None
    """
    # Standard CRC-32 generator polynomial in binary
    # Ref: https://lxp32.github.io/docs/a-simple-example-crc32-calculation/
    generator_polynomial = '100000100110000010001110110110111'

    num_experiments = 50
    min_burst_length = 32

    # Generate random binary number of 1520 bytes (12160 bits)
    data = generate_random_binary_string(1520 * 8)

    # Calculate transmitted message and CRC remainder
    transmitted_message, crc_remainder = crc(data, generator_polynomial)

    print(f"Transmitted message: {transmitted_message[:64]}...{transmitted_message[-64:]}")
    print(f"CRC remainder: {crc_remainder}")

    # Run experiments and store results in a DataFrame
    results = []
    for experiment_no in range(1, num_experiments + 1):
        burst_length = random.randint(min_burst_length + 1, min_burst_length + 100)  # Random length > 32 bits
        transmitted_message_with_error = introduce_burst_error(transmitted_message, burst_length)
        error_detected = not check_crc(transmitted_message_with_error, generator_polynomial)
        results.append((experiment_no, burst_length, 'Yes' if error_detected else 'No'))

    df = pd.DataFrame(results, columns=["Experiment No.", "Burst Error Length", "Error Detected (Yes/No)"])

    df.to_csv('crc_experiment_results.csv', index=False)

    print("\nExperiment Results:")
    print(df)


if __name__ == "__main__":
    main()
