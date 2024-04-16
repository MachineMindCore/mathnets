import igraph as ig
from typing import Any

def component_filter(source_graph: ig.Graph) -> ig.Graph:
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

def remove_isolated_nodes(source_graph: ig.Graph) -> ig.Graph:
    # Crear un subgrafo excluyendo los nodos aislados
    # Los nodos aislados tienen un grado de 0
    non_isolated_graph = source_graph.subgraph([v.index for v in source_graph.vs if source_graph.degree(v) > 0])

    return non_isolated_graph

def replace_none(source_graph: ig.Graph, replace_item: Any) -> ig.Graph:
    replaced_graph = source_graph
    for v in replaced_graph.vs:
        for key, value in v.attributes().items():
            if value is None:
                v[key] = replace_item
    return replaced_graph

def hubs_filter(source_graph: ig.Graph, *args, **kwargs) -> ig.Graph:
    degrees = source_graph.degree_distribution()

    print(degrees)
    return source_graph

def k_core_graph(source_graph: ig.Graph, k: int) -> ig.Graph:
    # Calcula los k-cores del grafo
    core_indices = source_graph.coreness()
    # Encuentra los vértices que cumplen con el grado mínimo k
    vertices_to_keep = [idx for idx, degree in enumerate(core_indices) if degree >= k]
    # Crea un subgrafo con los vértices seleccionados
    k_core_subgraph = source_graph.subgraph(vertices_to_keep)

    return k_core_subgraph