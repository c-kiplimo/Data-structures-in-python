queue =[]
def enqueue():
    element = input("Enter the element to be inserted: ")
    queue.append(element)
    print(element, "is inserted to the queue")

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        e = queue.pop(0)
        print("Removed element: ", e)

def display():
    print("Queue: ", queue)

while True:
    print("Select the operation 1. Enqueue 2. Dequeue 3. Display 4. Exit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Enter a valid choice")