from graph import Graph
from node import Node
from edge import Edge


def build_cell_network(graph_type):
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


g = build_cell_network(Graph)
print(g)

# CREATE TABLE restaurants(
#     id BIGSERIAL NOT NULL PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     street_address VARCHAR(50) NOT NULL,
#     city VARCHAR(50) NOT NULL,
#     zipcode VARCHAR(50) NOT NULL,
#     price_range INT NOT NULL check(price_range >= 1 and price_range <= 5),
#     food_type VARCHAR(50) NOT NULL
# )

# INSERT INTO restaurants(name, street_address, city, zipcode, price_range, food_type) values('Shake Shack', '2995 Larimer St', 'Denver', '80205', 2, 'fast casual')
