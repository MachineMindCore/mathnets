from mathnets.roadmap import make_container_index
from mathnets.containers import GraphHandler

DEMO_CONTAINER = "data/processed/proofwiki"

container = GraphHandler(DEMO_CONTAINER)

seed = container["pickle"]
container["index.json"] = make_container_index(seed)