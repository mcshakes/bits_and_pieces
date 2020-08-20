class Deque():
    def __init__(self):
        self.collection = []

    # left side
    def add_front(self, item):
        self.collection.insert(0, item)

    # right side
    def add_rear(self, item):
        self.collection.append(item)

    # remove from left side
    def remove_front(self):
        self.collection.pop()

    # remove from right side
    def remove_rear(self):
        del self.collection[-1]

    def is_empty(self):
        return self.collection == 0

    def size(self):
        return len(self.collection)
