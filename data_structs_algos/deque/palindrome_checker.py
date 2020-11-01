from deque import Deque


def pal_checker(inc_string):
    deque = Deque()

    for char in inc_string:
        deque.add_front(char)

    still_equal = True

    while deque.size() > 1:
        last = deque.remove_rear()
        first = deque.remove_front()

        if last != first:
            still_equal = False

    return still_equal
