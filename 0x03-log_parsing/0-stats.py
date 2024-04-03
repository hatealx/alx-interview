#!/usr/bin/python3
"""
Module for parsing statistics
"""
import signal
import sys

total_file_size = 0
status_code_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def prt_statistics():
    """Pratistics"""
    """Print statistics"""
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))


def signal_handler(sig, frame):
    """
    Sl handler function for signal. SIGINT
    """
    prt_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 7:
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
            except ValueError:
                continue

            # Update metrics
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1
            # Print statistics every 
            if line_count % 10 == 0:
                prt_statistics()

    prt_statistics()
except KeyboardInterrupt:
    prt_statistics()
    sys.exit(0)
