class Queue:
    def __init__(self):
        self.push_pile = []
        self.pull_pile = []

    def enqueue(self, value):
        self.push_pile.append(value)

    def deque(self):
        if not self.pull_pile:
            if not self.push_pile:
                print('Queue is already empty!')
                return

            while self.push_pile:
                self.pull_pile.append(self.push_pile.pop())

        return self.pull_pile.pop()


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
