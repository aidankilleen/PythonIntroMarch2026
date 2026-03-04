#!/usr/bin/env python3
import os
import sys
import argparse
import heapq
from typing import List, Tuple

def human_size(num_bytes: int) -> str:
    """Return a human-readable size (e.g., 12.3 MB)."""
    units = ["bytes", "KB", "MB", "GB", "TB", "PB"]
    size = float(num_bytes)
    for unit in units:
        if size < 1024 or unit == units[-1]:
            # Format bytes without decimals; others with 1 decimal place
            if unit == "bytes":
                return f"{int(size)} {unit}"
            return f"{size:.1f} {unit}"
        size /= 1024.0

def find_n_largest_files(start_dir: str, n: int, verbose: bool = False) -> List[Tuple[int, str]]:
    """
    Walk the directory tree rooted at start_dir and return the N largest files
    as a list of (size_in_bytes, full_path) tuples, sorted descending by size.
    Uses a min-heap for efficiency.
    """
    # Min-heap holding up to n items: (size, path)
    heap: List[Tuple[int, str]] = []

    for root, dirs, files in os.walk(start_dir):
        if verbose:
            print(f"Checking: {root}")

        for name in files:
            path = os.path.join(root, name)

            # Use lstat to avoid following symlinks; if you prefer following, use os.path.getsize
            try:
                # Skip broken symlinks or unreadable files
                if os.path.islink(path):
                    # For symlinks, try to get target size; if it fails, skip
                    try:
                        size = os.path.getsize(path)
                    except OSError:
                        continue
                else:
                    size = os.path.getsize(path)
            except OSError:
                continue

            if len(heap) < n:
                heapq.heappush(heap, (size, path))
            else:
                # If current file is larger than smallest in heap, replace it
                if size > heap[0][0]:
                    heapq.heapreplace(heap, (size, path))

    # Convert heap to a list sorted by size descending
    return sorted(heap, key=lambda t: t[0], reverse=True)

def positive_int(value: str) -> int:
    """argparse helper that ensures a positive integer >= 1."""
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid integer value: '{value}'")
    if ivalue < 1:
        raise argparse.ArgumentTypeError("Count must be >= 1")
    return ivalue

def main():
    parser = argparse.ArgumentParser(
        description="Find the N largest files in a directory tree."
    )

    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory to search (default: current directory)"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show directories as they are being checked"
    )

    parser.add_argument(
        "-n", "--count",
        type=positive_int,
        default=10,
        help="Number of largest files to list (default: 10)"
    )

    args = parser.parse_args()

    start_dir = args.directory

    if not os.path.isdir(start_dir):
        print(f"Error: '{start_dir}' is not a valid directory.")
        sys.exit(1)

    results = find_n_largest_files(start_dir, args.count, args.verbose)

    if not results:
        print("No files found in the directory tree.")
        return

    print(f"\nTop {len(results)} largest file(s) under: {os.path.abspath(start_dir)}\n")
    width = len(str(max(size for size, _ in results)))  # align bytes column

    for rank, (size, path) in enumerate(results, start=1):
        print(f"{rank:>2}. {str(size).rjust(width)} bytes  ({human_size(size):>9})  {path}")

if __name__ == "__main__":
    main()