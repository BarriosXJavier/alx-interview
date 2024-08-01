#!/usr/bin/python3
"""
Log parsing
"""

import sys

if __name__ == '__main__':

    total_file_size = 0
    count = 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """
        Print the statistics and file size.

        Args:
            stats (dict): A dictionary containing the statistics.
            file_size (int): The size of the file.

        Returns:
            None
        """
        print("File size: {:d}".format(file_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            data = line.split()

            # Ensure line matches the expected format
            if (len(data) != 7 or
                data[3][0] != '[' or
                data[4][-1] != ']' or
                data[5] != '"GET' or
                    data[6] != '/projects/260'):
                continue

            count += 1

            # Update status code count if it's valid
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except IndexError:
                continue

            # Update file size
            try:
                file_size = int(data[-1])
                total_file_size += file_size
            except (IndexError, ValueError):
                continue

            # Print stats every 10 lines
            if count % 10 == 0:
                print_stats(stats, total_file_size)

        # Print final stats
        print_stats(stats, total_file_size)

    except KeyboardInterrupt:
        print_stats(stats, total_file_size)
        raise
