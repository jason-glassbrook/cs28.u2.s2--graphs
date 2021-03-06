############################################################
#   GRAPH
#-----------------------------------------------------------
#   A simple implementation.
############################################################

from tools.data_structures import DefaultDict, Stack, Queue
from tools.iter_tools import is_iterable
from tools.debug_tools import debug_print

############################################################


def maybe_call(fun, args=None, kwargs=None):

    args = args or list()
    kwargs = kwargs or dict()

    if callable(fun):
        return fun(*args, **kwargs)

    return


############################################################
#   Graph
############################################################


class Graph:
    """
    Represent a graph as a mapping of node labels to edges.
    """

    DEFAULT__DEBUG = False

    # DEFAULT__ON_PUSH = None
    # DEFAULT__ON_POP = None
    DEFAULT__ON_VISIT = print

    def __init__(self, nodes=None, debug=DEFAULT__DEBUG):

        # yapf: disable
        def local_debug_print(*messages): debug_print("Graph.__init__", args=(nodes,), kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        self.__map = DefaultDict(set)

        if is_iterable(nodes):
            for n in nodes:
                self.add_node(n)

        return

    def get_map(self, debug=DEFAULT__DEBUG):

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).get_map", args=None, kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        return dict(self.__map)    # We don't want users to directly edit this.

    def get_nodes(self, debug=DEFAULT__DEBUG):

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).get_nodes", args=None, kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        return set(self.__map.keys())

    def get_edges(self, debug=DEFAULT__DEBUG):

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).get_edges", args=None, kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        return set((from_node, to_node)
                   for from_node in self.__map
                   for to_node in self.__map[from_node])

    def add_node(self, node, debug=DEFAULT__DEBUG):
        """
        Add a node with label `node` to the graph.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).add_node", args=(node,), kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        # Simply add the node in map with no neighbors.
        # If it already exists, there is no change.
        self.__map[node]

        return

    def add_edge(self, from_node, to_node, debug=DEFAULT__DEBUG):
        """
        Add a directed edge `(from_node, to_node)` to the graph.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).add_edge", args=(from_node, to_node,), kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        self.__map[from_node].add(to_node)

        return

    def get_neighbors(self, node, debug=DEFAULT__DEBUG):
        """
        Get all neighbors of the node with label `node`.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).get_neighbors", args=(node,), kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        return set(self.__map[node])    # We don't want users to directly edit this.

    def xft(
        self,
        PusherPopper,
        from_node,
        on_visit=DEFAULT__ON_VISIT,
        debug=DEFAULT__DEBUG,
    ):
        """
        Find each node in the graph from `from_node` in customizable order.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).xft", args=(PusherPopper, from_node,), kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        nodes_to_visit = PusherPopper()
        visited_nodes = set()
        traversed_nodes = list()

        nodes_to_visit.push(from_node)
        local_debug_print(f"pushed: {from_node}")

        while len(nodes_to_visit) > 0:

            node = nodes_to_visit.pop()
            local_debug_print(f"popped: {node}")

            if node not in visited_nodes:

                maybe_call(on_visit, [node])
                visited_nodes.add(node)
                traversed_nodes.append(node)
                local_debug_print(f"visited: {node}")

                for neighbor in self.get_neighbors(node):

                    nodes_to_visit.push(neighbor)
                    local_debug_print(f"pushed: {neighbor}")

            else:

                local_debug_print(f"already visited: {node}")

        return traversed_nodes

    def bft(
        self,
        from_node,
        on_visit=DEFAULT__ON_VISIT,
        debug=DEFAULT__DEBUG,
    ):
        """
        Print each node in breadth-first order beginning from `from_node`.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).bft", args=(from_node,), kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        return self.xft(Queue, from_node, debug=debug)

    def dft(
        self,
        from_node,
        on_visit=DEFAULT__ON_VISIT,
        debug=DEFAULT__DEBUG,
    ):
        """
        Print each node in depth-first order beginning from `from_node`.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).dft", args=(from_node,), kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        return self.xft(Stack, from_node, debug=debug)

    def dft_recursive(
        self,
        from_node,
        visited_nodes=None,
        traversed_nodes=None,
        on_visit=DEFAULT__ON_VISIT,
        debug=DEFAULT__DEBUG,
    ):
        """
        Print each node in depth-first order beginning from `from_node`.

        This should be done using recursion.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).dft_recursive", args=(from_node, visited_nodes, traversed_nodes), kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        visited_nodes = visited_nodes or set()
        traversed_nodes = traversed_nodes or list()

        maybe_call(on_visit, [from_node])
        visited_nodes.add(from_node)
        traversed_nodes = traversed_nodes + [from_node]
        local_debug_print(f"visited: {from_node}")

        for neighbor in self.get_neighbors(from_node):

            if neighbor not in visited_nodes:

                traversed_nodes = self.dft_recursive(
                    neighbor,
                    visited_nodes,
                    traversed_nodes,
                    debug=debug,
                )

        return traversed_nodes

    def xfs(
        self,
        PusherPopper,
        from_node,
        to_node,
        on_visit=DEFAULT__ON_VISIT,
        debug=DEFAULT__DEBUG,
    ):
        """
        Find a path in the graph from `from_node` to `to_node` in customizable order.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).xfs", args=(PusherPopper, from_node, to_node,), kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        paths_to_visit = PusherPopper()
        visited_nodes = set()
        searched_path = None

        if from_node == to_node:

            searched_path = [to_node]
            local_debug_print(f"found a path: {searched_path}")

        else:

            # unlike xft, this holds paths
            paths_to_visit.push([from_node])
            local_debug_print(f"pushed: {[from_node]}")

        while len(paths_to_visit) > 0 and searched_path is None:

            path = paths_to_visit.pop()
            local_debug_print(f"popped: {path}")

            node = path[-1]
            local_debug_print(f"latest node: {node}")

            if node not in visited_nodes:

                maybe_call(on_visit, [node])
                visited_nodes.add(node)
                local_debug_print(f"visited: {node}")

                for neighbor in self.get_neighbors(node):

                    neighbor_path = list(path)
                    neighbor_path.append(neighbor)

                    if neighbor == to_node:

                        searched_path = neighbor_path
                        local_debug_print(f"found a path: {searched_path}")
                        break

                    paths_to_visit.push(neighbor_path)
                    local_debug_print(f"pushed: {neighbor_path}")

            else:

                local_debug_print(f"already visited: {node}")

        return searched_path

    def bfs(
        self,
        from_node,
        to_node,
        on_visit=DEFAULT__ON_VISIT,
        debug=DEFAULT__DEBUG,
    ):
        """
        Return a list containing the shortest path from `from_node` to `to_node` in breath-first order.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).bfs", args=(from_node, to_node,), kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        return self.xfs(Queue, from_node, to_node, on_visit=on_visit, debug=debug)

    def dfs(
        self,
        from_node,
        to_node,
        on_visit=DEFAULT__ON_VISIT,
        debug=DEFAULT__DEBUG,
    ):
        """
        Return a list containing a path from `from_node` to `to_node` in depth-first order.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).dfs", args=(from_node, to_node,), kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        return self.xfs(Stack, from_node, to_node, on_visit=on_visit, debug=debug)

    def dfs_recursive(
        self,
        from_node,
        to_node,
        visited_nodes=None,
        searched_path=None,
        on_visit=DEFAULT__ON_VISIT,
        debug=DEFAULT__DEBUG
    ):
        """
        Return a list containing a path from `from_node` to `to_node` in depth-first order.

        This should be done using recursion.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).dfs_recursive", args=(from_node, to_node, visited_nodes, searched_path), kwargs=None, messages=messages, should_print=debug,); return # noqa
        # yapf: enable

        local_debug_print()

        visited_nodes = visited_nodes or set()
        searched_path = searched_path or list()

        maybe_call(on_visit, [from_node])
        visited_nodes.add(from_node)
        searched_path = searched_path + [from_node]
        local_debug_print(f"visited: {from_node}")

        if from_node == to_node:

            local_debug_print(f"found: {to_node}")
            return searched_path

        else:

            for neighbor in self.get_neighbors(from_node):

                if neighbor not in visited_nodes:

                    neighbor_path = self.dfs_recursive(
                        neighbor,
                        to_node,
                        visited_nodes,
                        searched_path,
                        debug=debug,
                    )

                    if neighbor_path is not None:

                        local_debug_print(
                            f"using neighbor's path: {neighbor}, {neighbor_path}"
                        )
                        return neighbor_path

                    else:

                        local_debug_print(f"not using neighbor's path: {neighbor}")

        local_debug_print(f"not found from: {from_node}")
        return None


if __name__ == "__main__":

    # Instantiate the graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    graph.add_node(6)
    graph.add_node(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    print(graph.get_map())
    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """

    print(graph.bft(1))
    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """

    print(graph.dft(1))
    print(graph.dft_recursive(1))
    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """

    print(graph.bfs(1, 6))
    """
    Valid BFS path:
        [1, 2, 4, 6]
    """

    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
