import igraph as ig
import pandas as pd
import matplotlib.pyplot as plt

from typing import Dict

def generate_graph_data(source_graph: ig.Graph, **kwargs) -> str:
    
    NAME = kwargs["name"]
    DIRECTED = source_graph.is_directed()
    NODES = source_graph.vcount()
    EDGES = source_graph.ecount()
    DENSITY = source_graph.density()
    DIAMETER = source_graph.diameter()
    AV_DEGREE = sum(source_graph.degree()) / NODES  # Average degree calculation

    summary_template = """
    ============================= SUMMARY =============================
    Name: {}
    Directed: {}
    Nodes: {}
    Edges: {}

    Density: {}
    Diameter: {}
    Av.Degree: {}
    -------------------------------------------------------------------
    """
    summary_data = summary_template.format(NAME, DIRECTED, NODES, EDGES, DENSITY, DIAMETER, AV_DEGREE)

    return summary_data

def generate_node_data(source_graph: ig.Graph, **kwargs) -> pd.DataFrame:
    degree_centrality = source_graph.degree()
    closeness_centrality = source_graph.closeness()
    betweenness_centrality = source_graph.betweenness()

    # Create a DataFrame with the centrality measures
    data = {
        'Node': range(source_graph.vcount()),
        'Degree Centrality': degree_centrality,
        'Closeness Centrality': closeness_centrality,
        'Betweenness Centrality': betweenness_centrality
    }
    nodes_df = pd.DataFrame(data)

    return nodes_df


def accumulate_distribution_plots(source_graph: ig.Graph, **kwargs) -> Dict[str, plt.]:
    degree
    