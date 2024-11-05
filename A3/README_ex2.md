# CRC Functions Test

This repository contains functions to calculate and verify Cyclic Redundancy Check (CRC) values, as well as a client program to test these functions using user input.

## Files

- `crc_functions.py`: Contains the `crc` and `check_crc` functions.
- `test_crc_functions.py`: A client program that accepts user input for the generator polynomial `G(x)` and message `M(x)`, calculates the transmitted message `P(x)`, and verifies the CRC.

## Requirements

- Python 3.x

## Usage

1. **Run the test client program:**

    ```bash
    python test_crc_functions.py
    ```

3. **Follow the prompts:**

    - Enter the generator polynomial `G(x)` in binary format.
    - Enter the message `M(x)` in binary format.

## Example

```bash
$ python test_crc_functions.py
CRC Calculation and Verification
Enter the generator polynomial G(x) in binary: 1011
Enter the message M(x) in binary: 110100111101
Transmitted message P(x) (message + CRC): 110100111101000
CRC remainder: 000
CRC verification result: valid
```
