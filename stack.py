# Implementation of the Stack in Python

# Code to implement the stack data structure
class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack content:", self.stack)

# Code to Perform Stack Operations
stack = Stack()

while True:
    print("Menu:")
    print("1. Push an item")
    print("2. Pop an item")
    print("3. Check if the stack is empty")
    print("4. Peek at the top item")
    print("5. Get the size of the stack")
    print("6. Print the entire content of the stack")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        item = input("Enter an item to push onto the stack: ")
        stack.push(item)
        print("Item pushed onto the stack:", item)
    elif choice == "2":
        item = stack.pop()
        if item is None:
            print("Stack is empty. Cannot pop an item.")
        else:
            print("Popped item:", item)
    elif choice == "3":
        if stack.is_empty():
            print("Stack is empty.")
        else:
            print("Stack is not empty.")
    elif choice == "4":
        item = stack.peek()
        if item is None:
            print("Stack is empty. No item to peek.")
        else:
            print("Top item:", item)
    elif choice == "5":
        if stack.is_empty():
            print("Stack is empty.")
        else:
            print("Size of the stack:", stack.size())
    elif choice == "6":
        if stack.is_empty():
            print("Stack is empty.")
        else:
            stack.display()
    elif choice == "7":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
    
    print()
