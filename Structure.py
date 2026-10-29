class Node:
    """A basic node class for a singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class ArrayStack:
    """Fixed-size stack implemented using a Python list."""
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.data) - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        value = self.data[self.top]
        self.data[self.top] = None  # Clear reference
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data[self.top]

    def __str__(self):
        if self.is_empty():
            return "Stack: []"
        elements = [str(self.data[i]) for i in range(self.top, -1, -1)]
        return f"Stack (top to bottom): -> {' -> '.join(elements)}"


class LinkedStack:
    """Dynamic-size stack implemented using a singly linked list at the head."""
    def __init__(self):
        self.top = None  # Head of the list matches the top of the stack

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False  # Linked lists do not have a fixed capacity

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.value

    def __str__(self):
        if self.is_empty():
            return "Stack: []"
        elements = []
        current = self.top
        while current:
            elements.append(str(current.value))
            current = current.next
        return f"Stack (top to bottom): -> {' -> '.join(elements)}"


class ArrayQueue:
    """Circular queue implemented using a fixed-size Python list."""
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow")
        rear = (self.front + self.size) % len(self.data)
        self.data[rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        value = self.data[self.front]
        self.data[self.front] = None  # Clear reference
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.data[self.front]

    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        elements = []
        for i in range(self.size):
            idx = (self.front + i) % len(self.data)
            elements.append(str(self.data[idx]))
        return f"Queue (front to rear): [{' -> '.join(elements)}]"


class LinkedQueue:
    """Queue implemented using a singly linked list with head and tail references."""
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None  # Prevent bad enqueues later
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.value

    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        elements = []
        current = self.front
        while current:
            elements.append(str(current.value))
            current = current.next
        return f"Queue (front to rear): [{' -> '.join(elements)}]"