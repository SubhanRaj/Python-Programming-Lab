# Demonstrate the usage of the Dictionary in Python

# Create an empty dictionary
my_dict = {}

# Add key-value pairs to the dictionary
my_dict["name"] = "John Doe"
my_dict["age"] = 25
my_dict["city"] = "New York"

# Access values in the dictionary
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])

# Modify values in the dictionary
my_dict["age"] = 30
print("Modified dictionary:", my_dict)

# Remove a key-value pair from the dictionary
removed_value = my_dict.pop("city")
print("Removed value:", removed_value)
print("Updated dictionary:", my_dict)

# Check if a key exists in the dictionary
if "name" in my_dict:
    print("The key 'name' exists in the dictionary.")
else:
    print("The key 'name' does not exist in the dictionary.")

# Get the keys and values in the dictionary
keys = my_dict.keys()
values = my_dict.values()
print("Keys:", keys)
print("Values:", values)

# Iterate over key-value pairs in the dictionary
print("Key-Value Pairs:")
for key, value in my_dict.items():
    print(key, ":", value)

# Clear the dictionary
my_dict.clear()
print("Cleared dictionary:", my_dict)
