import igraph as ig
import pandas as pd
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
    eigenvector_centrality = source_graph.eigenvector_centrality()

    # Create a DataFrame with the centrality measures
    data = {
        'Node': range(source_graph.vcount()),
        'Degree Centrality': degree_centrality,
        'Closeness Centrality': closeness_centrality,
        'Betweenness Centrality': betweenness_centrality,
        'Eigenvector Centrality': eigenvector_centrality
    }
    nodes_df = pd.DataFrame(data)

    return nodes_df


def generate_distribution_plots(source_graph: ig.Graph, **kwargs) -> Dict[str, plt.figure]:
    data = generate_node_data(source_graph)
    fig, axs = plt.subplots(2, 2, figsize=(16, 12))

    # Plot histograms for each centrality measure
    _, _, bars = axs[0,0].hist(data['Degree Centrality'], bins=20, color='skyblue', edgecolor='black')
    axs[0,0].set_title('Degree Centrality Distribution')
    axs[0,0].set_xlabel('Degree Centrality')
    axs[0,0].set_ylabel('Frequency')
    axs[0,0].bar_label(bars, fontsize=8, color='black')
    axs[0,0].set_yscale("log")

    _, _, bars = axs[0,1].hist(data['Closeness Centrality'], bins=20, color='salmon', edgecolor='black')
    axs[0,1].set_title('Closeness Centrality Distribution')
    axs[0,1].set_xlabel('Closeness Centrality')
    axs[0,1].set_ylabel('Frequency')
    axs[0,1].bar_label(bars, fontsize=8, color='black')
    axs[0,1].set_yscale("log")

    _, _, bars = axs[1,0].hist(data['Betweenness Centrality'], bins=20, color='coral', edgecolor='black')
    axs[1,0].set_title('Betweenness Centrality Distribution')
    axs[1,0].set_xlabel('Betweenness Centrality')
    axs[1,0].set_ylabel('Frequency')
    axs[1,0].bar_label(bars, fontsize=8, color='black')
    axs[1,0].set_yscale("log")

    _, _, bars = axs[1,1].hist(data['Eigenvector Centrality'], bins=20, color='lightgreen', edgecolor='black')
    axs[1,1].set_title('Eigenvector Centrality Distribution')
    axs[1,1].set_xlabel('Eigenvector Centrality')
    axs[1,1].set_ylabel('Frequency')
    axs[1,1].bar_label(bars, fontsize=8, color='black')
    axs[1,1].set_yscale("log")

    return fig

def get_hubs(graph: ig.Graph, n_hubs = 3):
    # Sort vertices by degree in descending order
    sorted_vertices = sorted(graph.vs, key=lambda x: x.degree(), reverse=True)

    # Get the IDs of the top num_hubs vertices
    hubs = dict()
    for node in sorted_vertices[:n_hubs]:
        hubs[int(node["id"])] = node["title"]

    return hubs

def get_categories(graph: ig.Graph) -> set:
    all_categories = set()
    for vertex in graph.vs:
        categories_update = vertex["toplevel_categories"]
        all_categories.update(categories_update)
    return all_categories