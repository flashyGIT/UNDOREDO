# Import the Node class you created in node.py
from node import Node


# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None

        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            return None

        return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return

        current = self.top

        while current is not None:
            print(current.data)
            current = current.next


def run_undo_redo():
   
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")

            # Push the action onto the undo stack
            undo_stack.push(action)

            # A new action clears the redo stack
            redo_stack = Stack()

            print(f"Action performed: {action}")

        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            action = undo_stack.pop()

            if action is None:
                print("Nothing to undo.")
            else:
                redo_stack.push(action)
                print(f"Undid action: {action}")

        elif choice == "3":
          
            action = redo_stack.pop()

            if action is None:
                print("Nothing to redo.")
            else:
                undo_stack.push(action)
                print(f"Redid action: {action}")

        elif choice == "4":
           
            print("\nUndo Stack:")
            undo_stack.display()

        elif choice == "5":
            
            print("\nRedo Stack:")
            redo_stack.display()

        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_undo_redo()
