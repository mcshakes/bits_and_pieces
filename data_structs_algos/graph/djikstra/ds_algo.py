# Breadth first search can be thought of as shortest, used with unweighted graphs
# Djikstra's can be thought of as the fastest,  used with weighted graphs

# Step1: find cheapest node

# Step 2: From that cheapest, see how long it takes to get to neighbors. At the same time, update the possible times to the finish line if possible

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}  # Finishing node dont have neighbors

# {'start': {'a': 6, 'b': 2}, 'a': {'fin': 1}, 'b': {'a': 3, 'fin': 5}, 'fin': {}}

infinity = float("inf")

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []


def find_lowest_cost_unprocessed(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


    # lowest cost node that is unprocessed
node = find_lowest_cost_unprocessed(costs)

while node is not None:  # if all nodes processed, this is done.
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():

        new_cost = cost + neighbors[n]

        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_unprocessed(costs)

# import code
#         code.interact(local=dict(globals(), **locals()))
