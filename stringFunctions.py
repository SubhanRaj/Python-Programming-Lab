# Program to Implement and Demonstrate String Functions in Python

# String functions demonstration

# Length of a string
def string_length(string):
    return len(string)

# Convert a string to uppercase
def uppercase(string):
    return string.upper()

# Convert a string to lowercase
def lowercase(string):
    return string.lower()

# Count the occurrences of a substring in a string
def count_substring(string, substring):
    return string.count(substring)

# Check if a string starts with a specific prefix
def starts_with(string, prefix):
    return string.startswith(prefix)

# Check if a string ends with a specific suffix
def ends_with(string, suffix):
    return string.endswith(suffix)

# Main program
input_string = input("Enter a string: ")

print("Length of the string:", string_length(input_string))
print("Uppercase:", uppercase(input_string))
print("Lowercase:", lowercase(input_string))

substring = input("Enter a substring to count: ")
print("Occurrences of the substring:", count_substring(input_string, substring))

prefix = input("Enter a prefix to check: ")
if starts_with(input_string, prefix):
    print("The string starts with the prefix.")
else:
    print("The string does not start with the prefix.")

suffix = input("Enter a suffix to check: ")
if ends_with(input_string, suffix):
    print("The string ends with the suffix.")
else:
    print("The string does not end with the suffix.")

