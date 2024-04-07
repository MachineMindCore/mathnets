import igraph as ig
import streamlit as st
import matplotlib.pyplot as plt

from typing import List, Dict, Any

class GraphExplorer:
    """
    Custom Widget to explore graph data as plot.

    Args:
        graph_meta: Dict[Any] => Structured metadata of graph (load and descriptive info)
    Notes:
        - graph_meta must point to conceptual graph (.gml, .grahpml, ...), full data byte stream should not be used in this context
    """
    def __init__(self, graph_meta: Dict[str, Any]) -> None:
        # Atributtes
        self.graph_meta = graph_meta
        self.graph = ig.Graph()
        
        # Initialization
        self._load()
        return
    
    def _load(self) -> None:
        self.graph = ig.read(self.graph_meta["address"])
        return
    
    def set_meta(self, **kargs) -> None:
        self.graph_meta = {**self.graph_meta, **kargs}
        return