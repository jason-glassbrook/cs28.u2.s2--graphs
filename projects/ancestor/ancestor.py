############################################################

from itertools import chain

from tools.iter_tools import reduce

from projects.graph.graph import Graph

############################################################

DEFAULT__DEBUG = False
DEFAULT__DEFAULT = -1    # ...because that's what the spec wants


def dict_item__max(a, b):

    key_a, value_a = a
    key_b, value_b = b

    if value_a is None:
        return b

    if value_b is None:
        return a

    if value_a >= value_b:
        return a

    else:
        return b


def earliest_ancestor(
    ancestor_edges,
    from_node,
    default=DEFAULT__DEFAULT,
    debug=DEFAULT__DEBUG,
):

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

    #===========================================================
    # OBVIOUS APPROACH
    #-----------------------------------------------------------
    # - Search from `from_node` to every other node
    # - Pick the longest path
    #-----------------------------------------------------------

    other_nodes = ancestors.get_nodes().difference({from_node})

    if debug:
        print("--- other nodes ---")
        print(other_nodes)

    ancestor_paths = {
        to_node: ancestors.bfs(from_node, to_node, on_visit=None)
        for to_node in other_nodes
    }

    if debug:
        print("--- ancestor paths ---")
        print(ancestor_paths)

    ancestor_distances = {
        to_node: len(path) if path else None
        for to_node, path in ancestor_paths.items()
    }

    if debug:
        print("--- ancestor distances ---")
        print(ancestor_distances)

    longest_path = reduce(dict_item__max, ancestor_distances.items())

    if debug:
        print("--- longest path ---")
        print(longest_path)

    if longest_path[1] is None:
        earliest_node = default
    else:
        earliest_node = longest_path[0]

    return earliest_node
