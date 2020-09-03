from graph import Graph
from vertex import Vertex
from queue.queue import Queue


def bfs(g, start):
    start.set_distance(0)
    start.set_pred(None)
    vert_queue = Queue()
    vert_queue.enqueue(start)

    while vert_queue.size() > 0:
        current_vert = vert_queue.dequeue()
