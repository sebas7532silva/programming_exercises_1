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
    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            value = line.strip()
            if not value:
                continue
            try:
                number = float(value)
                numbers.append(number)
            except ValueError:
                print(f"Invalid data on line {line_number}: '{value}'")
    return numbers


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
    """Compute mode using basic algorithm."""
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

    return mode_value


def compute_variance(numbers, mean):
    """Compute variance using basic algorithm."""
    total = 0.0
    for num in numbers:
        total += (num - mean) ** 2
    return total / len(numbers)


def compute_std_dev(variance):
    """Compute standard deviation using basic algorithm."""
    return variance ** 0.5


def main():
    """Main execution function."""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
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

    mean = compute_mean(numbers)
    median = compute_median(numbers)
    mode = compute_mode(numbers)
    variance = compute_variance(numbers, mean)
    std_dev = compute_std_dev(variance)

    elapsed_time = time.time() - start_time

    results = (
        "Descriptive Statistics\n"
        "----------------------\n"
        f"Count: {len(numbers)}\n"
        f"Mean: {mean}\n"
        f"Median: {median}\n"
        f"Mode: {mode}\n"
        f"Variance: {variance}\n"
        f"Standard Deviation: {std_dev}\n"
        f"Elapsed Time: {elapsed_time:.6f} seconds\n"
    )

    print(results)

    with open("StatisticsResults.txt", "w", encoding="utf-8") as output:
        output.write(results)


if __name__ == "__main__":
    main()
