#!/usr/bin/python3
import sys
import re


def print_data(total_file_size, status_code_data):
    """Prints total size and status code count"""
    print("File size: {}".format(total_file_size))
    for k, v in sorted(status_code_data.items()):
        if v != 0:
            print("{}: {}".format(k, v))


status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
status_code_data = {code: 0 for code in status_codes}
total_file_size = 0
count = 0

log_pattern = re.compile(
    r'\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
)

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            code, size = match.groups()
            total_file_size += int(size)
            if code in status_code_data:
                status_code_data[code] += 1
            count += 1
            if count % 10 == 0:
                print_data(total_file_size, status_code_data)
except KeyboardInterrupt:
    print_data(total_file_size, status_code_data)
    raise
except Exception as e:
    pass
finally:
    print_data(total_file_size, status_code_data)
