#!/usr/bin/python3

"""UTF-8 Validation script"""

def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    bytes_remaining = 0

    for byte in data:
        binary_byte = format(byte, '#010b')[-8:]

        if bytes_remaining == 0:
            for bit in binary_byte:
                if bit == '0':
                    break
                bytes_remaining += 1

            if bytes_remaining == 0:
                continue

            if bytes_remaining == 1 or bytes_remaining > 4:
                return False
        else:
            if not (binary_byte[0] == '1' and binary_byte[1] == '0'):
                return False

        bytes_remaining -= 1

    return bytes_remaining == 0
