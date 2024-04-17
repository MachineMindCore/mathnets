import igraph as ig
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from typing import Dict

def generate_graph_data(source_graph: ig.Graph, **kwargs) -> str:
    
    NAME = kwargs["name"]
    DIRECTED = source_graph.is_directed()
    NODES = source_graph.vcount()
    EDGES = source_graph.ecount()
    
    THEOREMS_COUNT = len(source_graph.vs.select(lambda node: node["type"] == "theorem"))
    DEFINITIONS_COUNT = len(source_graph.vs.select(lambda node: node["type"] == "definition"))
    OTHERS_COUNT = len(source_graph.vs.select(lambda node: node["type"] == "other"))
    
    DENSITY = source_graph.density()
    DIAMETER = source_graph.diameter()
    AV_DEGREE = sum(source_graph.degree()) / NODES  # Average degree calculation

    summary_template = """
    ============================= SUMMARY =============================
    # Metadata
    Name: {}
    Directed: {}
    Nodes: {}
    Edges: {}

    # Types
    Theorems: {}
    Definitions: {}
    Others: {}

    # Measures
    Density: {}
    Diameter: {}
    Av.Degree: {}
    -------------------------------------------------------------------
    """
    summary_data = summary_template.format(
        NAME, 
        DIRECTED, 
        NODES, 
        EDGES, 
        THEOREMS_COUNT, 
        DEFINITIONS_COUNT, 
        OTHERS_COUNT,  
        DENSITY, 
        DIAMETER, 
        AV_DEGREE
    )

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


def generate_distribution_plots(source_graph: ig.Graph, **kwargs) -> Dict[str, plt.figure]:
    data = generate_node_data(source_graph)
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))

    # Plot histograms for each centrality measure
    _, _, bars = axs[0].hist(data['Degree Centrality'], bins=20, color='skyblue', edgecolor='black')
    axs[0].set_title('Degree Centrality Distribution')
    axs[0].set_xlabel('Degree Centrality')
    axs[0].set_ylabel('Frequency')
    axs[0].bar_label(bars, fontsize=8, color='black')
    axs[0].set_yscale("log")

    _, _, bars = axs[1].hist(data['Closeness Centrality'], bins=20, color='salmon', edgecolor='black')
    axs[1].set_title('Closeness Centrality Distribution')
    axs[1].set_xlabel('Closeness Centrality')
    axs[1].set_ylabel('Frequency')
    axs[1].bar_label(bars, fontsize=8, color='black')
    axs[1].set_yscale("log")

    _, _, bars = axs[2].hist(data['Betweenness Centrality'], bins=20, color='lightgreen', edgecolor='black')
    axs[2].set_title('Betweenness Centrality Distribution')
    axs[2].set_xlabel('Betweenness Centrality')
    axs[2].set_ylabel('Frequency')
    axs[2].bar_label(bars, fontsize=8, color='black')
    axs[2].set_yscale("log")

    return fig
    