# Demonstrate the usage of the List in Python

# Create an empty list
my_list = []

# Add elements to the list
my_list.append("apple")
my_list.append("banana")
my_list.append("orange")

# Access elements in the list
print("First element:", my_list[0])
print("Second element:", my_list[1])
print("Last element:", my_list[-1])

# Modify elements in the list
my_list[1] = "grape"
print("Modified list:", my_list)

# Remove elements from the list
removed_item = my_list.pop(0)
print("Removed item:", removed_item)
print("Updated list:", my_list)

# Get the length of the list
list_length = len(my_list)
print("Length of the list:", list_length)

# Check if an element exists in the list
if "orange" in my_list:
    print("The element 'orange' exists in the list.")
else:
    print("The element 'orange' does not exist in the list.")

# Iterate over the elements in the list
print("Elements in the list:")
for item in my_list:
    print(item)

# Clear the list
my_list.clear()
print("Cleared list:", my_list)
