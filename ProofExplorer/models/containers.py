from models.references import GraphReference
from igraph import Graph


class GraphMachine:
    def __init__(self, container_addr: str) -> None:
        self.reference = GraphReference(container_addr)
        return 
    