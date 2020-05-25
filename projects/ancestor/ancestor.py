############################################################

from itertools import chain

from projects.graph.graph import Graph

############################################################


def earliest_ancestor(ancestor_edges, from_node):

    # Define `ancestors` graph from `ancestor_edges`...
    ancestors = Graph()

    # Define nodes:
    ancestor_nodes = set(chain.from_iterable(ancestor_edges))
    for node in ancestor_nodes:
        ancestors.add_node(node)

    # Define edges:
    for parent, child in ancestor_edges:
        # child -> parent
        ancestors.add_edge(parent, child)

    print(ancestors.get_map())

    return
