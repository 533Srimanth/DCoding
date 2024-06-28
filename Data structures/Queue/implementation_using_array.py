class FixedSizeQueue:
    def __init__(self, size):
        self.size = size
        self.arr = [None]*size
        self.start = 0
        self.end = 0
        self.curr_size = 0

    def enqueue_with_raises(self, value):
        if self.curr_size == self.size:
            raise Exception('Queue is already full!')

        self.arr[self.end] = value
        self.end = (self.end + 1) % self.size
        self.curr_size += 1

    def enqueue(self, value):
        try:
            self.enqueue_with_raises(value)
        except Exception as e:
            print(str(e))

    def deque_with_raises(self):
        if self.curr_size == 0:
            print('Queue is already empty!')
            return

        temp = self.arr[self.start]
        self.start = (self.start + 1) % self.size
        self.curr_size -= 1

        return temp

    def deque(self):
        try:
            return self.deque_with_raises()
        except Exception as e:
            print(str(e))


class DynamicQueue:
    def __init__(self):
        self.curr_total_size = 100
        self.queue = FixedSizeQueue(self.curr_total_size)

    def enqueue(self, value):
        try:
            self.queue.enqueue_with_raises(value)
        except Exception:
            self.curr_total_size *= 2
            temp_queue = FixedSizeQueue(self.curr_total_size)

            while True:
                try:
                    temp_queue.enqueue(self.queue.deque_with_raises())
                except Exception:
                    break

            temp_queue.enqueue(value)
            self.queue = temp_queue

    def deque(self):
        return self.queue.deque()


class Queue:
    def __init__(self, size=0):
        if size == 0:
            self.queue = DynamicQueue()
        else:
            self.queue = FixedSizeQueue(size)

    def enqueue(self, value):
        self.queue.enqueue(value)

    def deque(self):
        return self.queue.deque()


if __name__ == '__main__':
    print('Dynamic size queue')
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

    print('\nFixed size queue')
    queue = Queue(2)

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
