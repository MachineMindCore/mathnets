from igraph import Graph
from naturalproofs_toolkit.containers import GraphContainer
from naturalproofs_toolkit.roadmap import make_roadmap

class RoadMapper:
    def __init__(self, base_addr: str) -> None:
        self.base_container = GraphContainer(base_addr)
        self.base_graph = self.base_container.load()
        self.roadmap_id = ""
        return

    def map(self, from_id: int, to_id: int) -> None:
        self.roadmap_id = f"{from_id}-{to_id}"
        roadmap_name = f"{self.base_container.name}_{self.roadmap_id}"
        roadmap = make_roadmap(self.base_graph, from_id, to_id)
        roadmap_container = GraphContainer(f"data/roadmaps/{roadmap_name}")
        roadmap_container.seed(roadmap)
        roadmap_container.build()
        return
    
    def get(self, roadmap_id: str) -> Graph:
        roadmap_name = f"{self.base_container.name}_{roadmap_id}"
        roadmap_container = GraphContainer(f"data/roadmaps/{roadmap_name}")
        roadmap = roadmap_container.load()
        return roadmap
    
        
