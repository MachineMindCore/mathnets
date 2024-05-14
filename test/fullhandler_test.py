from naturalproofs_toolkit.containers import GraphHandler

SEED_ADDR = "data/raw/naturalproofs_proofwiki"
TEST_ADDR = "data/test/raw_test"

seed_handler = GraphHandler(SEED_ADDR)
seed_graph = seed_handler["pickle"]

test_handler = GraphHandler(TEST_ADDR)
test_handler["pickle"] = seed_graph
test_handler.build()