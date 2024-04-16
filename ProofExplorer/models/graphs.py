from models.references import GraphReference
from igraph import Graph


class GraphContainer:
    def __init__(self, container_addr: str) -> None:
        self.reference = GraphReference(container_addr)
        return 
    
    def procces