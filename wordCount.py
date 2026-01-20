# pylint: disable=invalid-name
"""
Count distinct words and their frequency from a file.

Usage:
    python wordCount.py fileWithData.txt
"""

import sys
import time


def read_words(file_path):
    """Read words from a file, handling invalid data."""
    words = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            try:
                clean_line = line.strip()
                if not clean_line:
                    continue

                parts = clean_line.split()
                for part in parts:
                    word = part.strip()
                    if word:
                        words.append(word.lower())
            except Exception as exc:  # pylint: disable=broad-except
                print(f"Error on line {line_number}: {exc}")
    return words


def count_words(words):
    """Count frequency of each distinct word using basic algorithm."""
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


def main():
    """Main execution function."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    try:
        words = read_words(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)

    if not words:
        print("No valid words found.")
        sys.exit(1)

    frequency = count_words(words)

    lines = []
    lines.append("Row Labels\tCount")
    lines.append("-------------------------")

    total = 0
    sorted_items = sorted(
        frequency.items(),
        key=lambda item: (-item[1], item[0])
    )

    for word, count in sorted_items:
        lines.append(f"{word}\t{count}")
        total += count

    lines.append("")
    lines.append(f"Grand Total\t{total}")

    elapsed_time = time.time() - start_time
    lines.append("")
    lines.append(f"Elapsed Time: {elapsed_time:.6f} seconds")

    result_text = "\n".join(lines)

    print(result_text)

    with open("WordCountResults.txt", "w", encoding="utf-8") as output:
        output.write(result_text)


if __name__ == "__main__":
    main()
