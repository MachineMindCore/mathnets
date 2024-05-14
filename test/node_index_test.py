from naturalproofs_toolkit.roadmap import make_container_index
from naturalproofs_toolkit.containers import GraphHandler

DEMO_CONTAINER = "data/processed/proofwiki"

container = GraphHandler(DEMO_CONTAINER)

seed = container["pickle"]
container["index.json"] = make_container_index(seed)