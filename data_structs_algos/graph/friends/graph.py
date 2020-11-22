from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johnny"]

graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johnny"] = []


def search():
    search_queue = deque()
    search_queue += graph["you"]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):  # Run function check here
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

            print("People already searched ", searched)

    return False


def person_is_seller(name):
    return name[-1] == "m"


search()
