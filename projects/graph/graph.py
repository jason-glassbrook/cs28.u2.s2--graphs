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

    DEFAULT_DEBUG = False

    def __init__(self, nodes=None, debug=DEFAULT_DEBUG):

        debug_print("Graph.__init__", (nodes), should_print=debug)

        self.__map = DefaultDict(set)

        if is_iterable(nodes):
            for n in nodes:
                self.add_node(n)

        return

    @property
    def map(self):

        return dict(self.__map)    # We don't want users to directly edit this.

    @property
    def nodes(self):

        return set(self.__map.keys())

    @property
    def edges(self):

        return set((from_node, to_node)
                   for from_node in self.__map
                   for to_node in self.__map[from_node])

    def add_node(self, node, debug=DEFAULT_DEBUG):
        """
        Add a node with label `node` to the graph.
        """

        debug_print("Graph.add_node", (node), should_print=debug)

        # Simply add the node in map with no neighbors.
        # If it already exists, there is no change.
        self.__map[node]

        return

    def add_edge(self, from_node, to_node, debug=DEFAULT_DEBUG):
        """
        Add a directed edge `(from_node, to_node)` to the graph.
        """

        debug_print("Graph.add_edge", (from_node, to_node), should_print=debug)

        self.__map[from_node].add(to_node)

        return

    def get_neighbors(self, node, debug=DEFAULT_DEBUG):
        """
        Get all neighbors of the node with label `node`.
        """

        debug_print("Graph.get_neighbors", (node), should_print=debug)

        return set(self.__map[node])    # We don't want users to directly edit this.

    def bft(self, from_node, debug=DEFAULT_DEBUG):
        """
        Print each node in breadth-first order beginning from `from_node`.
        """

        debug_print("Graph.bft", (from_node), should_print=debug)

        return

    def dft(self, from_node, debug=DEFAULT_DEBUG):
        """
        Print each node in depth-first order beginning from `from_node`.
        """

        debug_print("Graph.dft", (from_node), should_print=debug)

        return

    def dft_recursive(self, from_node, debug=DEFAULT_DEBUG):
        """
        Print each node in depth-first order beginning from `from_node`.

        This should be done using recursion.
        """

        debug_print("Graph.dft_recursive", (from_node), should_print=debug)

        return

    def bfs(self, from_node, to_node, debug=DEFAULT_DEBUG):
        """
        Return a list containing the shortest path from `from_node` to `to_node` in breath-first order.
        """

        debug_print("Graph.bfs", (from_node, to_node), should_print=debug)

        return

    def dfs(self, from_node, to_node, debug=DEFAULT_DEBUG):
        """
        Return a list containing a path from `from_node` to `to_node` in depth-first order.
        """

        debug_print("Graph.dfs", (from_node, to_node), should_print=debug)

        return

    def dfs_recursive(self, from_node, to_node, debug=DEFAULT_DEBUG):
        """
        Return a list containing a path from `from_node` to `to_node` in depth-first order.

        This should be done using recursion.
        """

        debug_print("Graph.dfs_recursive", (from_node, to_node), should_print=debug)

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

    print(graph.vertices)
    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """

    graph.bft(1)
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

    graph.dft(1)
    graph.dft_recursive(1)
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
