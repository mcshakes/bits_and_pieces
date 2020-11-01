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
        return self.collection.pop(0)

    # remove from right side
    def remove_rear(self):
        return self.collection.pop()

    def is_empty(self):
        return self.collection == 0

    def size(self):
        return len(self.collection)
