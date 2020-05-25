############################################################

from itertools import chain

from projects.graph.graph import Graph

############################################################

DEFAULT__DEBUG = False


def earliest_ancestor(ancestor_edges, from_node, debug=DEFAULT__DEBUG):

    # Define `ancestors` graph from `ancestor_edges`...
    ancestors = Graph()

    # Define nodes:
    ancestor_nodes = set(chain.from_iterable(ancestor_edges))
    for node in ancestor_nodes:
        ancestors.add_node(node)

    # Define edges:
    for parent, child in ancestor_edges:
        # child -> parent
        ancestors.add_edge(child, parent)

    if debug:
        print("--- ancestors ---")
        print(ancestors.get_map())

    return
