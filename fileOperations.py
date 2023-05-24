# Perform read and write operations on files in Python

import os

# Write data to a file
def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            file.write(data)
        print("Data written to the file successfully.")
    except IOError:
        print("Error: Failed to write data to the file.")

# Read data from a file
def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            print("Data read from the file:", data)
    except IOError:
        print("Error: Failed to read data from the file.")

# Check if the file exists
def check_file_exists(file_name):
    return os.path.isfile(file_name)

# Get file name from the user
file_name = input("Enter the file name: ")

# Check if the file exists
if check_file_exists(file_name):
    # File exists, prompt for operation choice
    while True:
        print("Choose an operation:")
        print("1. Read from the file")
        print("2. Write to the file")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            read_from_file(file_name)
        elif choice == "2":
            data_to_write = input("Enter the data to write to the file: ")
            write_to_file(file_name, data_to_write)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    # File doesn't exist, ask if the user wants to create it
    create_file = input("File doesn't exist. Do you want to create it? (y/n): ")

    if create_file.lower() == "y":
        data_to_write = input("Enter the data to write to the file: ")
        write_to_file(file_name, data_to_write)
    else:
        print("Exiting the program.")
