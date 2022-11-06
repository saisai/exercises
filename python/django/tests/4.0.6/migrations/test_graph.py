from django.db.migrations.exceptions import CircularDependencyError, NodeNotFoundError
from django.db.migrations.graph import DummyNode, MigrationGraph, Node
from django.test import SimpleTestCase

class GraphTests(SimpleTestCase):
    """
    Tests the digraph structure.
    """
    def test_simple_graph(self):
        """
        Tests a basic dependency graph:
        app_a: 0001 <-- 0002 <--- 0003 <-- 0004
        app_b: 0001 <-- 0002 <-/
        """
        # Build graph
        graph = MigrationGraph()
        graph.add_node(("app_a", "0001"), None)
        graph.add_node(("app_a", "0002"), None)
        graph.add_node(("app_a", "0003"), None)
        graph.add_node(("app_a", "0004"), None)
        graph.add_node(("app_b", "0001"), None)
        graph.add_node(("app_b", "0002"), None)
        graph.add_dependency("app_a.0004", ("app_a", "0004"), ("app_a", "0003"))
        graph.add_dependency("app_a.0003", ("app_a", "0003"), ("app_a", "0002"))
        graph.add_dependency("app_a.0002", ("app_a", "0002"), ("app_a", "0001"))
        graph.add_dependency("app_a.0003", ("app_a", "0003"), ("app_b", "0002"))
        graph.add_dependency("app_b.0002", ("app_b", "0002"), ("app_b", "0001"))
        # Test root migration case
        print(graph.forwards_plan(("app_a", "0001")))
        self.assertEqual(
                graph.forwards_plan(("app_a", "0001")),
                [("app_a", "0001")],
                )
        # Test branch B only
        print(graph.forwards_plan(("app_b", "0002")))
        self.assertEqual(
                graph.forwards_plan(("app_b", "0002")),
                [("app_b", "0001"), ("app_b", "0002")],
                )

        # Test whole graph
        self.assertEqual(
            graph.forwards_plan(("app_a", "0004")),
            [
                ("app_b", "0001"),
                ("app_b", "0002"),
                ("app_a", "0001"),
                ("app_a", "0002"),
                ("app_a", "0003"),
                ("app_a", "0004"),
            ],
        )
        # Test reverse to b:0002
        self.assertEqual(
            graph.backwards_plan(("app_b", "0002")),
            [("app_a", "0004"), ("app_a", "0003"), ("app_b", "0002")],
        )
        # Test roots and leaves
        self.assertEqual(
            graph.root_nodes(),
            [("app_a", "0001"), ("app_b", "0001")],
        )
        self.assertEqual(
            graph.leaf_nodes(),
            [("app_a", "0004"), ("app_b", "0002")],
        )
    
    def test_complex_graph(self):
        r"""
        Tests a complex dependency graph:

        app_a:  0001 <-- 0002 <--- 0003 <-- 0004
                      \        \ /         /
        app_b:  0001 <-\ 0002 <-X         /
                      \          \       /
        app_c:         \ 0001 <-- 0002 <-
        """
        # Build graph
        graph = MigrationGraph()
        graph.add_node(("app_a", "0001"), None)
        graph.add_node(("app_a", "0002"), None)
        graph.add_node(("app_a", "0003"), None)
        graph.add_node(("app_a", "0004"), None)
        graph.add_node(("app_b", "0001"), None)
        graph.add_node(("app_b", "0002"), None)
        graph.add_node(("app_c", "0001"), None)
        graph.add_node(("app_c", "0002"), None)
        graph.add_dependency("app_a.0004", ("app_a", "0004"), ("app_a", "0003"))
        graph.add_dependency("app_a.0003", ("app_a", "0003"), ("app_a", "0002"))
        graph.add_dependency("app_a.0002", ("app_a", "0002"), ("app_a", "0001"))
        graph.add_dependency("app_a.0003", ("app_a", "0003"), ("app_b", "0002"))
        graph.add_dependency("app_b.0002", ("app_b", "0002"), ("app_b", "0001"))
        graph.add_dependency("app_a.0004", ("app_a", "0004"), ("app_c", "0002"))
        graph.add_dependency("app_c.0002", ("app_c", "0002"), ("app_c", "0001"))
        graph.add_dependency("app_c.0001", ("app_c", "0001"), ("app_b", "0001"))
        graph.add_dependency("app_c.0002", ("app_c", "0002"), ("app_a", "0002"))
        # Test branch C only

        print(graph.forwards_plan(("app_c", "0002")))

        self.assertEqual(
            graph.forwards_plan(("app_c", "0002")),
            [
                ("app_b", "0001"),
                ("app_c", "0001"),
                ("app_a", "0001"),
                ("app_a", "0002"),
                ("app_c", "0002"),
            ],
        )
        # Test whole graph
        self.assertEqual(
            graph.forwards_plan(("app_a", "0004")),
            [
                ("app_b", "0001"),
                ("app_c", "0001"),
                ("app_a", "0001"),
                ("app_a", "0002"),
                ("app_c", "0002"),
                ("app_b", "0002"),
                ("app_a", "0003"),
                ("app_a", "0004"),
            ],
        )
        # Test reverse to b:0001

        print(graph.backwards_plan(("app_b", "0001")))
        self.assertEqual(
            graph.backwards_plan(("app_b", "0001")),
            [
                ("app_a", "0004"),
                ("app_c", "0002"),
                ("app_c", "0001"),
                ("app_a", "0003"),
                ("app_b", "0002"),
                ("app_b", "0001"),
            ],
        )

        # Test roots and leaves
        self.assertEqual(
            graph.root_nodes(),
            [("app_a", "0001"), ("app_b", "0001"), ("app_c", "0001")],
        )
        self.assertEqual(
            graph.leaf_nodes(),
            [("app_a", "0004"), ("app_b", "0002"), ("app_c", "0002")],
        )

    def test_circular_graph(self):
        """
        Tests a circular dependency graph.
        """
        # Build graph
        graph = MigrationGraph()
        graph.add_node(("app_a", "0001"), None)
        graph.add_node(("app_a", "0002"), None)
        graph.add_node(("app_a", "0003"), None)
        graph.add_node(("app_b", "0001"), None)
        graph.add_node(("app_b", "0002"), None)
        graph.add_dependency("app_a.0003", ("app_a", "0003"), ("app_a", "0002"))
        graph.add_dependency("app_a.0002", ("app_a", "0002"), ("app_a", "0001"))
        graph.add_dependency("app_a.0001", ("app_a", "0001"), ("app_b", "0002"))
        graph.add_dependency("app_b.0002", ("app_b", "0002"), ("app_b", "0001"))
        graph.add_dependency("app_b.0001", ("app_b", "0001"), ("app_a", "0003"))
        # Test whole graph
        #graph.ensure_not_cyclic()
        with self.assertRaises(CircularDependencyError):
            graph.ensure_not_cyclic()

    def test_circular_graph_2(self):
        graph = MigrationGraph()
        graph.add_node(("A", "0001"), None)
        graph.add_node(("C", "0001"), None)
        graph.add_node(("B", "0001"), None)
        graph.add_dependency("A.0001", ("A", "0001"), ("B", "0001"))
        graph.add_dependency("B.0001", ("B", "0001"), ("A", "0001"))
        graph.add_dependency("C.0001", ("C", "0001"), ("B", "0001"))

        with self.assertRaises(CircularDependencyError):
            graph.ensure_not_cyclic()


