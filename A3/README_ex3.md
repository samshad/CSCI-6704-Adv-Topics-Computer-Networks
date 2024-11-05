# CRC Functions Test with Burst Error Experiment

This is a client program to conduct an experiment with burst errors.

## Files

- `crc_functions.py`: Contains the `crc` and `check_crc` functions.
- `error_functions.py`: Contains the `introduce_error` and `generate_random_binary_string` functions.

## Requirements

- Python 3.x
- Pandas library (install via `pip install pandas`)

## Usage

1. **Run the test client program:**

    ```bash
    python error_detection_crc.py
    ```

## Example

```bash
$ python test_crc_functions.py
Transmitted message: 1101111111100111000100100110001110011110011111000001010001011110...0111010111011011010111000110101101010001111011101111011011100001
CRC remainder: 01010001111011101111011011100001

Experiment Results:
    Experiment No.  Burst Error Length Error Detected (Yes/No)
0                1                  77                     Yes
1                2                  90                     Yes
2                3                  99                     Yes
3                4                  81                     Yes
4                5                 132                     Yes
5                6                  85                     Yes
6                7                  74                     Yes
7                8                  58                     Yes
8                9                  61                     Yes
...
49              50                  78                     Yes
