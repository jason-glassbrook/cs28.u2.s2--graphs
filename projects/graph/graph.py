############################################################
#   GRAPH
#-----------------------------------------------------------
#   A simple implementation.
############################################################

from tools.data_structures import DefaultDict, Stack, Queue
from tools.iter_tools import is_iterable
from tools.debug_tools import debug_print

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
    # DEFAULT__ON_VISIT = None

    def __init__(self, nodes=None, debug=DEFAULT__DEBUG):

        # yapf: disable
        def local_debug_print(*messages): debug_print("Graph.__init__", args=(nodes,), kwargs=None, messages=messages, should_print=debug,); return
        # yapf: enable

        local_debug_print()

        self.__map = DefaultDict(set)

        if is_iterable(nodes):
            for n in nodes:
                self.add_node(n)

        return

    def get_map(self, debug=DEFAULT__DEBUG):

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).get_map", args=None, kwargs=None, messages=messages, should_print=debug,); return
        # yapf: enable

        local_debug_print()

        return dict(self.__map)    # We don't want users to directly edit this.

    def get_nodes(self, debug=DEFAULT__DEBUG):

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).get_nodes", args=None, kwargs=None, messages=messages, should_print=debug,); return
        # yapf: enable

        local_debug_print()

        return set(self.__map.keys())

    def get_edges(self, debug=DEFAULT__DEBUG):

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).get_edges", args=None, kwargs=None, messages=messages, should_print=debug,); return
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
        def local_debug_print(*messages): debug_print("(Graph).add_node", args=(node,), kwargs=None, messages=messages, should_print=debug,); return
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
        def local_debug_print(*messages): debug_print("(Graph).add_edge", args=(from_node, to_node,), kwargs=None, messages=messages, should_print=debug,); return
        # yapf: enable

        local_debug_print()

        self.__map[from_node].add(to_node)

        return

    def get_neighbors(self, node, debug=DEFAULT__DEBUG):
        """
        Get all neighbors of the node with label `node`.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).get_neighbors", args=(node,), kwargs=None, messages=messages, should_print=debug,); return
        # yapf: enable

        local_debug_print()

        return set(self.__map[node])    # We don't want users to directly edit this.

    def xft(self, PusherPopper, from_node, debug=DEFAULT__DEBUG):
        """
        Print each node in customizable order beginning from `from_node`.
        """

        ON_VISIT = print

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).xft", args=(PusherPopper, from_node,), kwargs=None, messages=messages, should_print=debug,); return
        # yapf: enable

        local_debug_print()

        nodes_to_visit = PusherPopper()
        visited_nodes = set()
        visited_path = list()

        nodes_to_visit.push(from_node)

        local_debug_print(f"pushed: {from_node}")

        while len(nodes_to_visit) > 0:

            node = nodes_to_visit.pop()
            local_debug_print(f"popped: {node}")

            if node not in visited_nodes:

                ON_VISIT(node)
                visited_nodes.add(node)
                visited_path.append(node)
                local_debug_print(f"visited: {node}")

                for neighbor in self.get_neighbors(node):

                    nodes_to_visit.push(neighbor)
                    local_debug_print(f"pushed: {neighbor}")

            else:

                local_debug_print(f"already visited: {node}")

        return visited_path

    def bft(self, from_node, debug=DEFAULT__DEBUG):
        """
        Print each node in breadth-first order beginning from `from_node`.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).bft", args=(from_node,), kwargs=None, messages=messages, should_print=debug,); return
        # yapf: enable

        local_debug_print()

        return self.xft(Queue, from_node, debug=debug)

    def dft(self, from_node, debug=DEFAULT__DEBUG):
        """
        Print each node in depth-first order beginning from `from_node`.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).dft", args=(from_node,), kwargs=None, messages=messages, should_print=debug,); return
        # yapf: enable

        local_debug_print()

        return self.xft(Stack, from_node, debug=debug)

    def dft_recursive(self, from_node, debug=DEFAULT__DEBUG):
        """
        Print each node in depth-first order beginning from `from_node`.

        This should be done using recursion.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).dft_recursive", args=(from_node,), kwargs=None, messages=messages, should_print=debug,); return
        # yapf: enable

        local_debug_print()

        return

    def bfs(self, from_node, to_node, debug=DEFAULT__DEBUG):
        """
        Return a list containing the shortest path from `from_node` to `to_node` in breath-first order.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).bfs", args=(from_node, to_node,), kwargs=None, messages=messages, should_print=debug,); return
        # yapf: enable

        local_debug_print()

        return

    def dfs(self, from_node, to_node, debug=DEFAULT__DEBUG):
        """
        Return a list containing a path from `from_node` to `to_node` in depth-first order.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).dfs", args=(from_node, to_node,), kwargs=None, messages=messages, should_print=debug,); return
        # yapf: enable

        local_debug_print()

        return

    def dfs_recursive(self, from_node, to_node, debug=DEFAULT__DEBUG):
        """
        Return a list containing a path from `from_node` to `to_node` in depth-first order.

        This should be done using recursion.
        """

        # yapf: disable
        def local_debug_print(*messages): debug_print("(Graph).dfs_recursive", args=(from_node, to_node,), kwargs=None, messages=messages, should_print=debug,); return
        # yapf: enable

        local_debug_print()

        return


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
