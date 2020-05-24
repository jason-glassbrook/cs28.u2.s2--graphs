############################################################

import unittest
import sys
import io

from .graph import Graph

############################################################


class Test(unittest.TestCase):

    def setUp(self):

        self.__sys_stdout = sys.stdout
        sys.stdout = io.StringIO()

        self.graph = Graph()

        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_node(3)
        self.graph.add_node(4)
        self.graph.add_node(5)
        self.graph.add_node(6)
        self.graph.add_node(7)

        self.graph.add_edge(5, 3)
        self.graph.add_edge(6, 3)
        self.graph.add_edge(7, 1)
        self.graph.add_edge(4, 7)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(7, 6)
        self.graph.add_edge(2, 4)
        self.graph.add_edge(3, 5)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(4, 6)

        return

    def tearDown(self):

        sys.stdout = self.__sys_stdout

        return

    def test_nodes(self):

        nodes = {
            1: {2},
            2: {3, 4},
            3: {5},
            4: {6, 7},
            5: {3},
            6: {3},
            7: {1, 6},
        }

        self.assertDictEqual(self.graph.get_map(), nodes)

        return

    def test_bft(self):

        bft = [
            "1\n2\n3\n4\n5\n6\n7\n",
            "1\n2\n3\n4\n5\n7\n6\n",
            "1\n2\n3\n4\n6\n7\n5\n",
            "1\n2\n3\n4\n6\n5\n7\n",
            "1\n2\n3\n4\n7\n6\n5\n",
            "1\n2\n3\n4\n7\n5\n6\n",
            "1\n2\n4\n3\n5\n6\n7\n",
            "1\n2\n4\n3\n5\n7\n6\n",
            "1\n2\n4\n3\n6\n7\n5\n",
            "1\n2\n4\n3\n6\n5\n7\n",
            "1\n2\n4\n3\n7\n6\n5\n",
            "1\n2\n4\n3\n7\n5\n6\n",
        ]

        self.graph.bft(1)

        output = sys.stdout.getvalue()

        self.assertIn(output, bft)

        return

    def test_dft(self):

        dft = [
            "1\n2\n3\n5\n4\n6\n7\n",
            "1\n2\n3\n5\n4\n7\n6\n",
            "1\n2\n4\n7\n6\n3\n5\n",
            "1\n2\n4\n6\n3\n5\n7\n",
        ]

        self.graph.dft(1)

        output = sys.stdout.getvalue()

        self.assertIn(output, dft)

        return

    def test_dft_recursive(self):

        dft = [
            "1\n2\n3\n5\n4\n6\n7\n",
            "1\n2\n3\n5\n4\n7\n6\n",
            "1\n2\n4\n7\n6\n3\n5\n",
            "1\n2\n4\n6\n3\n5\n7\n",
        ]

        self.graph.dft_recursive(1)

        output = sys.stdout.getvalue()

        self.assertIn(output, dft)

        return

    def test_bfs(self):

        bfs = [1, 2, 4, 6]
        self.assertListEqual(self.graph.bfs(1, 6), bfs)

        return

    def test_dfs(self):

        dfs = [[1, 2, 4, 6], [1, 2, 4, 7, 6]]
        self.assertIn(self.graph.dfs(1, 6), dfs)

        return

    def test_dfs_recursive(self):

        dfs = [[1, 2, 4, 6], [1, 2, 4, 7, 6]]
        self.assertIn(self.graph.dfs_recursive(1, 6), dfs)

        return


if __name__ == "__main__":
    unittest.main()
