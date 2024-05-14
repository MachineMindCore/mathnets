import unittest
from igraph import Graph
from naturalproofs_toolkit.containers import GraphHandler

DEMO_ADDR = "data/raw/naturalproofs_proofwiki"

class TestHandler (unittest.TestCase):

    def test_instance(self):
        handler = GraphHandler(DEMO_ADDR)
        self.assertIsInstance(handler, GraphHandler)
    
    def test_load(self):
        handler = GraphHandler(DEMO_ADDR)
        self.assertIsInstance(handler["pickle"], Graph)
    
    def test_save(self):
        handler = GraphHandler(DEMO_ADDR)
        handler["lgl"] = handler["pickle"]
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
