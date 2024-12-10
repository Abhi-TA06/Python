#write a python program to print the contents of a directory using the os module. search online 

import os

# Specify the directory path
directory_path = '/'

# List all contents of the directory
try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
