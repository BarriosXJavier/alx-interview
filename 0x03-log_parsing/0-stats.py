#!/usr/bin/env python3
import sys
import signal
import re

"""
Reads standard input line by line and computes metrics.
"""

def print_stats(total_size, status_codes):
    """Print statistics."""
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    pattern = re.compile(r'^(\S+) - \[(.+)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$')

    def signal_handler(sig, frame):
        """Handle keyboard interrupt."""
        print_stats(total_size, status_codes)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    for line in sys.stdin:
        match = pattern.match(line.strip())
        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()