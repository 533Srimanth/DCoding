class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def deque(self):
        if self.head is None:
            print('Queue is already empty!')
            return

        temp = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        return temp


if __name__ == '__main__':
    queue = Queue()

    queue.deque()

    queue.enqueue(1)
    print(queue.deque())
    queue.deque()

    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.deque())
    print(queue.deque())
    print(queue.deque())
    queue.deque()
