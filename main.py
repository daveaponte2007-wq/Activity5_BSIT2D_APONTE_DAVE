from structures import ArrayStack, LinkedStack, ArrayQueue, LinkedQueue

def check_balanced_parentheses(text):
    """Application Exercise 6a: Checks if a string of parentheses is balanced using a Stack."""
    stack = LinkedStack()
    pairs = {")": "(", "]": "[", "}": "{"}
    
    for char in text:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs.keys():
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()


def run_print_queue_simulation():
    """Application Exercise 6b: Simulates a printer queue using a Queue."""
    queue = LinkedQueue()
    print("\n--- Starting Print Queue Simulation ---")
    
    # Enqueue print jobs (Job ID, Page Count)
    jobs = [("Job_A", 4), ("Job_B", 15), ("Job_C", 2)]
    for job_id, pages in jobs:
        queue.enqueue((job_id, pages))
        print(f"Enqueued to print: {job_id} ({pages} pages)")
        
    print(f"Current Queue Status: {queue}")
    
    # Dequeue and process jobs in FIFO order
    wait_order = 1
    while not queue.is_empty():
        job_id, pages = queue.dequeue()
        print(f"[Wait Order #{wait_order}] Currently printing {job_id}...")
        wait_order += 1
    print("All print jobs have been processed successfully.\n")


def run_interactive_menu():
    """Menu-driven interface for interacting with data structures."""
    print("Choose a Data Structure to Interact With:")
    print("1. ArrayStack (Fixed Size: 3)")
    print("2. LinkedStack (Dynamic Size)")
    print("3. ArrayQueue (Circular, Fixed Size: 3)")
    print("4. LinkedQueue (Dynamic Size)")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        ds = ArrayStack(3)
        is_stack = True
    elif choice == '2':
        ds = LinkedStack()
        is_stack = True
    elif choice == '3':
        ds = ArrayQueue(3)
        is_stack = False
    elif choice == '4':
        ds = LinkedQueue()
        is_stack = False
    else:
        print("Invalid choice entered.")
        return

    while True:
        print(f"\nCurrent State: {ds}")
        print("Select an Operation:")
        if is_stack:
            print("1. Push (Insert Element)")
            print("2. Pop (Remove Element)")
            print("3. Peek (View Top Element)")
        else:
            print("1. Enqueue (Join Back of Queue)")
            print("2. Dequeue (Leave Front of Queue)")
            print("3. Peek Front (View Front Element)")
        print("4. Exit and Continue to Applications")
        
        op = input("Enter operation number: ")
        
        try:
            if op == '1':
                val = input("Type a value to insert: ")
                if is_stack:
                    ds.push(val)
                else:
                    ds.enqueue(val)
            elif op == '2':
                removed = ds.pop() if is_stack else ds.dequeue()
                print(f"Successfully removed element: {removed}")
            elif op == '3':
                peeked = ds.peek() if is_stack else ds.peek_front()
                print(f"The top/front element is: {peeked}")
            elif op == '4':
                break
            else:
                print("Invalid operation choice.")
        except (IndexError, OverflowError) as e:
            print(f"\n[EXPECTED ERROR CAUGHT]: {e}")


if _name_ == "_main_":
    print("=== DEMONSTRATION OF ERROR HANDLING & WRAP-AROUND ===")
    
    # Demonstrating ArrayStack Underflow & Overflow
    print("\n[Testing ArrayStack Error Handling]")
    stack_demo = ArrayStack(2)
    try:
        stack_demo.pop()  # Attempting to pop an empty stack
    except IndexError as e:
        print(f"-> Caught expected Underflow: {e}")
        
    stack_demo.push("First")
    stack_demo.push("Second")
    try:
        stack_demo.push("Third")  # Attempting to push to a full stack
    except OverflowError as e:
        print(f"-> Caught expected Overflow: {e}")

    # Demonstrating ArrayQueue Wrap-Around Behavior
    print("\n[Testing Circular Queue Wrap-Around]")
    queue_demo = ArrayQueue(3)
    queue_demo.enqueue("X")
    queue_demo.enqueue("Y")
    queue_demo.enqueue("Z")
    print(f"Queue is now full: {queue_demo}")
    print(f"Left the queue (Dequeue): {queue_demo.dequeue()}") # Index 0 becomes free
    queue_demo.enqueue("W") # Wraps around to physical index 0 using modulo
    print(f"After circular enqueue: {queue_demo}")
    
    print("\n=== ENTERING INTERACTIVE MENU ===")
    run_interactive_menu()
    
    print("\n=== APPLICATION EXERCISE 6a (BALANCED PARENTHESES) ===")
    test_strings = ["{[()]}", "{[(])}"]
    for s in test_strings:
        print(f"Is the string '{s}' balanced? -> {check_balanced_parentheses(s)}")
        
    print("\n=== APPLICATION EXERCISE 6b (PRINT QUEUE SIMULATION) ===")
    run_print_queue_simulation()