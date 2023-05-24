# Program for Implementing Squential Search in Python
def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element
    return -1  # Return -1 if the target is not found

# Get the size of the list from the user
size = int(input("Enter the size of the list: "))

# Get the elements of the list from the user
my_list = []
elements_input = input("Enter the elements separated by spaces: ")
elements = elements_input.split()
for element in elements:
    my_list.append(int(element))

# Get the target number from the user
target_number = int(input("Enter the target number: "))

# Perform sequential search
result = sequential_search(my_list, target_number)

if result != -1:
    print(f"{target_number} found at index {result}")
else:
    print("Target not found in the list")

