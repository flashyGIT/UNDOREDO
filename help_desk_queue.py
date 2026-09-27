# Import the Node class you created in node.py
from node import Node


# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)

       
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        
        if self.is_empty():
            return None

        
        data = self.front.data

       
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return data

    def peek(self):
      
        if self.is_empty():
            return None

        return self.front.data

    def display(self):
       
        current = self.front

        if current is None:
            print("No customers are waiting.")
            return

        while current is not None:
            print(current.data)
            current = current.next


def run_help_desk():
    
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")

            
            queue.enqueue(name)

            print(f"{name} added to the queue.")

        elif choice == "2":
           
            customer = queue.dequeue()

            if customer is None:
                print("No customers are waiting.")
            else:
                print(f"Helping {customer}.")

        elif choice == "3":
           
            customer = queue.peek()

            if customer is None:
                print("No customers are waiting.")
            else:
                print(f"Next customer: {customer}")

        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.display()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_help_desk()
