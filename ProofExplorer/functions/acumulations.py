from requests import get
from helpers.graphs import get_categories

import igraph as ig
import numpy as np
from typing import Dict, Generator, Tuple

def accumulate_top_categories(source_graph: ig.Graph, **kwargs) -> Generator[Tuple[str, ig.Graph], None, None]:       

    # Obtén todas las categorías de nivel superior únicas en el grafo
    all_categories = get_categories(source_graph)
    for category in all_categories:
        vertex_subset = source_graph.vs.select(lambda node: (node["type"] in ["definition", "other"]) or (category in node["top_categories"]))
        subgraph = source_graph.induced_subgraph(vertex_subset)
    
        # Add subgraphs to generator
        yield category, subgraph

def accumulate_graph_data(source_graph: ig.Graph, **kwargs):

    container_addr = kwargs["container_addr"]

    all_categories = get_categories(source_graphs)
    
    
      yield

def accumulate_node_data():
      yield

def accumulate_distribution_plots():
      yield