from graph import Graph
from node import Node
from edge import Edge


def build_friend_network(graph_type):
    network = graph_type()  # the incoming graph type
    names = ("Mike - Adam Selene", "Manny - Bob", "Prof - Billy", "Wyoh - Beth", "Cindy",
             "Chuck", "Chubb", "Carlos", "Candice", "Charro", "Carly", "Callie", "Cassie")

    for name in names:
        network.add_node(Node(name))

    network.add_edge(Edge(network.get_node("Mike - Adam Selene"),
                          network.get_node("Manny - Bob"))),
    network.add_edge(Edge(network.get_node("Mike - Adam Selene"),
                          network.get_node("Prof - Billy"))),
    network.add_edge(Edge(network.get_node("Mike - Adam Selene"),
                          network.get_node("Wyoh - Beth"))),

    network.add_edge(Edge(network.get_node("Manny - Bob"),
                          network.get_node("Chuck"))),

    network.add_edge(Edge(network.get_node("Manny - Bob"),
                          network.get_node("Chubb"))),

    network.add_edge(Edge(network.get_node("Manny - Bob"),
                          network.get_node("Carlos"))),

    network.add_edge(Edge(network.get_node("Prof - Billy"),
                          network.get_node("Candice"))),

    network.add_edge(Edge(network.get_node("Prof - Billy"),
                          network.get_node("Charro"))),

    network.add_edge(Edge(network.get_node("Prof - Billy"),
                          network.get_node("Carly"))),

    network.add_edge(Edge(network.get_node("Wyoh - Beth"),
                          network.get_node("Cindy"))),

    network.add_edge(Edge(network.get_node("Wyoh - Beth"),
                          network.get_node("Callie"))),

    network.add_edge(Edge(network.get_node("Wyoh - Beth"),
                          network.get_node("Cassie"))),

    return network


g = build_friend_network(Graph)
print(g)
