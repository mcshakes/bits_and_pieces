
def binary_search(my_list, item):
    first = 0
    last = len(my_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if my_list[midpoint] == item:
            found = True
        else:
            if item < my_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


def recursive_binary_search(my_list, item):
    if len(my_list) == 0:
        return False

    else:
        midpoint = len(my_list) // 2

        if my_list[midpoint] == item:
            return True
        else:
            if item < my_list[midpoint]:
                return recursive_binary_search(my_list[:midpoint], item)
            else:
                return recursive_binary_search(my_list[midpoint + 1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, 56]
# print(binary_search(testlist, 3))
# print(binary_search(testlist, 13))

print(recursive_binary_search(testlist, 3))
print(recursive_binary_search(testlist, 13))
