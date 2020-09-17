from graph import Graph
from node import Node
from edge import Edge


def build_friend_network(graph_type):
    network = graph_type()  # the incoming graph type
    names = ("Shelly", "Billy", "Zoe", "Chuckles", "Franziska", "Phelipe")

    for name in names:
        network.add_node(Node(name))

    network.add_edge(Edge(network.get_node("Shelly"),
                          network.get_node("Chuckles")))
    network.add_edge(Edge(network.get_node(
        "Phelipe"), network.get_node("Billy")))
    network.add_edge(Edge(network.get_node("Shelly"), network.get_node("Zoe")))
    network.add_edge(Edge(network.get_node("Billy"),
                          network.get_node("Franziska")))

    return network


g = build_friend_network(Graph)
print(g)
