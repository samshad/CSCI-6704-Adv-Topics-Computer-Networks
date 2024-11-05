"""Md Samshad Rahman"""
"""B00968344"""

import matplotlib.pyplot as plt
import numpy as np


def plot_waveform(binary_string, title, encoding_type):
    time = np.arange(0, len(binary_string) * 2, 1)
    waveform_points = []

    if encoding_type == "unipolar":
        for bit in binary_string:
            if bit == '1':
                waveform_points.extend([1, 1])
            else:
                waveform_points.extend([0, 0])

    elif encoding_type == "nrz":
        for bit in binary_string:
            if bit == '1':
                waveform_points.extend([1, 1])
            else:
                waveform_points.extend([-1, -1])

    elif encoding_type == "manchester":
        for bit in binary_string:
            if bit == '1':
                waveform_points.extend([1, -1])
            else:
                waveform_points.extend([-1, 1])

    plt.step(time, waveform_points, where='post')
    plt.ylim(-2, 2)
    plt.title(f'{title} Waveform')
    plt.text(0.5, 1.1, f'Input Binary String: {binary_string}', fontsize=12, ha='center', va='center',
             transform=plt.gca().transAxes)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    binary_string = input("Binary string: ")

    plot_waveform(binary_string, "Unipolar Encoding", "unipolar")
    plot_waveform(binary_string, "NRZ Encoding", "nrz")
    plot_waveform(binary_string, "Manchester Encoding", "manchester")


if __name__ == "__main__":
    main()

# Sample Input: 00110100010
# Sample Input: 101010101
# Sample Input: 1110001110
