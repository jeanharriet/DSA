class CircularQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0          # index of the first element
        self.rear = -1          # index of the last element
        self.size = 0           # number of elements currently stored

    # ---------- Status checks ----------
    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def __len__(self):
        return self.size

    # ---------- main operations ----------
    def enqueue(self, item):
        """Add an item at the rear. O(1)"""
        if self.is_full():
            raise OverflowError("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        """Remove and return the item at the front. O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        """Return the front item without removing it. O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    # ---------- Display ----------
    def display(self):
        """Print elements from front to rear (logical order)."""
        if self.is_empty():
            print("Queue is empty")
            return
        items = []
        for i in range(self.size):
            items.append(self.queue[(self.front + i) % self.capacity])
        print("Queue (front → rear):", items)

    def show_internal(self):
        """Show the raw array plus pointers, useful for learning."""
        print(f"Array: {self.queue} | front={self.front} "
              f"rear={self.rear} size={self.size}")


# ---------- illustration ----------
if __name__ == "__main__":
    cq = CircularQueue(5)

    print("--- Fill with 3 items ---")
    for x in (40, 60, 80):
        cq.enqueue(x)
    cq.show_internal()

    print("\n--- Dequeue one ---")
    print("Removed:", cq.dequeue())
    cq.show_internal()

    print("\n--- Enqueue until the rear wraps around ---")
    for x in (100, 120, 140):
        cq.enqueue(x)
        cq.show_internal()

    print("\n--- Try to overflow ---")
    try:
        cq.enqueue(160)
    except OverflowError as e:
        print("Error:", e)

    print("\n--- Logical view ---")
    cq.display()
    print("Front item:", cq.peek())

    print("\n--- Drain the queue ---")
    while not cq.is_empty():
        print("Dequeued:", cq.dequeue())

    try:
        cq.dequeue()
    except IndexError as e:
        print("Error:", e)