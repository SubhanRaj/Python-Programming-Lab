# Implement Selection Sort in Python

def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Get the size of the list from the user
size = int(input("Enter the size of the list: "))

# Get the elements of the list from the user
my_list = []
elements_input = input("Enter the elements separated by spaces: ")
elements = elements_input.split()
for element in elements:
    my_list.append(int(element))

print("Original list:", my_list)

selection_sort(my_list)
print("Sorted list:", my_list)
