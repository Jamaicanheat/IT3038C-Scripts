import os
import sys

# Set the minimum file size to search for (in bytes)
min_size = 200 * 1024 * 1024


# Define a function to search for files larger than the minimum size
def find_large_files(start_path):
    for dirpath, dirnames, filenames in os.walk(start_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                size = os.path.getsize(file_path)
                if size > min_size:
                    print(f"{file_path} ({size / (1024 * 1024):.2f} MB)")
            except OSError:
                continue


# Get the root directory of the system drive
drive = os.path.splitdrive(sys.executable)[0]

# Search for large files starting at the root directory
find_large_files(drive + "/")
