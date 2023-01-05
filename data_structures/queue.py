class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, val):
        self.q.append((val))

    def is_empty(self):
        return len(q)==0

    def dequeue(self):
        if q:
            return self.q.pop(0)
        else:
            raise Exception("Queue is empty")
