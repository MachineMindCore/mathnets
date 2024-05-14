from naturalproofs_toolkit.roadmap import make_roadmap, RoadMapper
from naturalproofs_toolkit.containers import GraphContainer

def roadmap_pipeline(graph_addr: str, from_id: int, to_id: int):
    roadmapper = RoadMapper(graph_addr)
    roadmapper.map(from_id, to_id)
