# pylint: disable=invalid-name
"""
Convert numbers from a file to binary and hexadecimal.

Usage:
    python convertNumbers.py fileWithData.txt
"""

import sys
import time


def read_numbers(file_path):
    """Read numbers from a file, handling invalid data."""
    numbers = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            value = line.strip()
            if not value:
                continue
            try:
                number = int(value)
                numbers.append(number)
            except ValueError:
                numbers.append(value)
    return numbers


def to_binary(number):
    """
    Positive:
        normal binary, no leading zeros.
    Negative:
        two's complement using the MINIMUM number of bits needed
        (but keeping the sign bit = 1).
    """
    if number == 0:
        return "0"

    # Positive -> normal binary
    if number > 0:
        return format(number, "b")

    # Negative -> minimal two's complement
    # bits needed for magnitude + 1 sign bit
    bits = abs(number).bit_length() + 1
    mask = (1 << bits) - 1
    value = number & mask
    return format(value, "b")


def to_hex(number):
    """
    Positive:
        normal hex, no leading zeros.
    Negative:
        32-bit two's complement (8 hex digits).
    """
    if number == 0:
        return "0"

    if number > 0:
        return format(number, "X")

    value = number & 0xFFFFFFFF
    return format(value, "08X")


def main():
    """Main execution function."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    try:
        numbers = read_numbers(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

    if not numbers:
        print("No valid numeric data found.")
        sys.exit(1)

    lines = []

    for num in numbers:
        try:
            binary = to_binary(num)
            hexa = to_hex(num)
            lines.append(f"{num}\t{binary}\t{hexa}")
        except ValueError:
            lines.append(f"{num}\t#VALUE!\t#VALUE!")

    elapsed_time = time.time() - start_time
    lines.append("")
    lines.append(f"Elapsed Time: {elapsed_time:.6f} seconds")

    result_text = "\n".join(lines)

    print(result_text)

    with open("P2/results/ConvertionResults.txt", "w", encoding="utf-8") as output:
        output.write(result_text)


if __name__ == "__main__":
    main()
