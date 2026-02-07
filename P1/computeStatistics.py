# pylint: disable=invalid-name

"""
Compute descriptive statistics from a file.

Usage:
    python computeStatistics.py fileWithData.txt
"""

import sys
import time


def read_numbers(file_path):
    """Read numbers from a file, handling invalid data."""
    numbers = []
    not_numbers = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            value = line.strip()
            if not value:
                continue
            try:
                number = float(value)
                numbers.append(number)
            except ValueError:
                not_numbers.append(value)
    return numbers, not_numbers


def compute_mean(numbers):
    """Compute mean using basic algorithm."""
    total = 0.0
    for num in numbers:
        total += num
    return total / len(numbers)


def compute_median(numbers):
    """Compute median using basic algorithm."""
    sorted_nums = sorted(numbers)
    count = len(sorted_nums)
    mid = count // 2

    if count % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]


def compute_mode(numbers):
    """Compute mode using basic algorithm. Return 'NA' if no mode exists."""
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_count = 0
    mode_value = None
    for key, value in frequency.items():
        if value > max_count:
            max_count = value
            mode_value = key

    if max_count == 1:
        return "#N/D"

    return mode_value



def compute_variance(numbers, mean):
    """Compute variance using basic algorithm."""
    total = 0.0
    for num in numbers:
        total += (num - mean) ** 2
    return total / (len(numbers) - 1)


def compute_std_dev(numbers, mean):
    """Compute standard deviation directly from the data (population)."""
    total = 0.0
    for num in numbers:
        total += (num - mean) ** 2
    return (total / len(numbers)) ** 0.5


def main():
    """Main execution function."""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    try:
        numbers, not_numbers = read_numbers(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

    if not numbers:
        print("No valid numeric data found.")
        sys.exit(1)

    mean = compute_mean(numbers)
    median = compute_median(numbers)
    mode = compute_mode(numbers)
    variance = compute_variance(numbers, mean)
    std_dev = compute_std_dev(numbers, mean)

    elapsed_time = time.time() - start_time

    results = (
        "Descriptive Statistics\n"
        "----------------------\n"
        f"Count: {len(numbers) + len(not_numbers)}\n"
        f"Mean: {mean}\n"
        f"Median: {median}\n"
        f"Mode: {mode}\n"
        f"Variance: {variance}\n"
        f"Standard Deviation: {std_dev}\n"
        f"Elapsed Time: {elapsed_time:.6f} seconds\n"
    )

    print(results)

    with open("P1/results/StatisticsResults.txt", "w", encoding="utf-8") as output:
        output.write(results)


if __name__ == "__main__":
    main()
