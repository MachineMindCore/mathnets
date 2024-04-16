import igraph as ig

def unconnected_filter(source_graph: ig.Graph) -> ig.Graph:
    # Find the connected components
    components = source_graph.components()
    # Get the largest connected component
    largest_component_idx = max(range(len(components)), key=lambda i: len(components[i]))
    largest_component = components.subgraph(largest_component_idx)

    # Create a new graph with only the largest connected component
    filtered_graph = ig.Graph(directed=source_graph.is_directed())
    filtered_graph.add_vertices(largest_component.vcount())
    filtered_graph.add_edges(largest_component.get_edgelist())

    return filtered_graph

def hubs_filter(source_graph: ig.Graph, *args, **kwargs) -> ig.Graph:
    degrees = source_graph.degree_distribution()

    print(degrees)
    return source_graph