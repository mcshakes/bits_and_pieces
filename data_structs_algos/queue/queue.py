import random


class Queue:
    def __init__(self):
        self.collection = []

    def enqueue(self, item):
        self.collection.insert(0, item)

    def dequeue(self):
        return self.collection.pop()

    def size(self):
        return len(self.collection)

# Queue class implementation


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1

            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def startNext(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60/self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp
