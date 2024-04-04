#!/usr/bin/python3

"""
Module: utf8_validation
This module provides a method for validating UTF-8 encoding in a given data set.
"""

def validUTF8(data):
    """
    Check if the given data set represents a valid UTF-8 encoding.

    Args:
    - data (list): A list of integers representing bytes of data.

    Returns:
    - bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Helper function to check if a byte is a valid UTF-8 leading byte
    def is_leading_byte(byte):
        return (byte >> 6) != 0b10

    # Iterate through each byte in the data set
    i = 0
    while i < len(data):
        # Count the number of bytes for the current UTF-8 character
        if (data[i] & 0b10000000) == 0:  # 1-byte character
            length = 1
        elif (data[i] & 0b11100000) == 0b11000000:  # 2-byte character
            length = 2
        elif (data[i] & 0b11110000) == 0b11100000:  # 3-byte character
            length = 3
        elif (data[i] & 0b11111000) == 0b11110000:  # 4-byte character
            length = 4
        else:
            return False  # Invalid leading byte

        # Check if the remaining bytes are valid continuation bytes
        for j in range(1, length):
            if i + j >= len(data) or (data[i + j] & 0b11000000) != 0b10000000:
                return False  # Invalid continuation byte
        i += length

    return True
