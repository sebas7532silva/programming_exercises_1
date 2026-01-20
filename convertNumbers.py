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
        for line_number, line in enumerate(file, start=1):
            value = line.strip()
            if not value:
                continue
            try:
                number = int(value)
                numbers.append(number)
            except ValueError:
                print(f"Invalid data on line {line_number}: '{value}'")
    return numbers


def to_binary(number):
    """Convert an integer to binary using basic algorithm."""
    if number == 0:
        return "0"

    is_negative = number < 0
    num = abs(number)
    digits = []

    while num > 0:
        digits.append(str(num % 2))
        num //= 2

    result = "".join(reversed(digits))
    if is_negative:
        result = "-" + result
    return result


def to_hexadecimal(number):
    """Convert an integer to hexadecimal using basic algorithm."""
    if number == 0:
        return "0"

    hex_map = "0123456789ABCDEF"
    is_negative = number < 0
    num = abs(number)
    digits = []

    while num > 0:
        digits.append(hex_map[num % 16])
        num //= 16

    result = "".join(reversed(digits))
    if is_negative:
        result = "-" + result
    return result


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
    lines.append("Number Conversion Results")
    lines.append("-------------------------")

    for num in numbers:
        binary = to_binary(num)
        hexa = to_hexadecimal(num)
        line = f"{num} -> Binary: {binary}, Hexadecimal: {hexa}"
        lines.append(line)

    elapsed_time = time.time() - start_time
    lines.append("")
    lines.append(f"Elapsed Time: {elapsed_time:.6f} seconds")

    result_text = "\n".join(lines)

    print(result_text)

    with open("ConvertionResults.txt", "w", encoding="utf-8") as output:
        output.write(result_text)


if __name__ == "__main__":
    main()
