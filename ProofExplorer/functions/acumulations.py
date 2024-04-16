import igraph as ig
import numpy as np
from typing import Dict, Generator, List, Tuple


def accumulate_categories(source_graph: ig.Graph, category_tab: str) -> Generator[Tuple[str, ig.Graph], None, None]:       

        # Obtén todas las categorías de nivel superior únicas en el grafo
        all_categories = set()
        for vertex in source_graph.vs:
            categories_update = vertex[category_tab]
            all_categories.update(categories_update)

        for category in all_categories:
            vertex_subset = source_graph.vs.select(lambda node: (node["type"] in ["definition", "other"]) or (category in node[category_tab]))
            subgraph = source_graph.induced_subgraph(vertex_subset)
        
            # Add subgraphs to generator
            yield category, subgraph

def accumulate_categories_isolated(source_graph: ig.Graph, category_tab: str) -> Generator[Tuple[str, ig.Graph], None, None]:       

        # Obtén todas las categorías de nivel superior únicas en el grafo
        all_categories = set()
        for vertex in source_graph.vs:
            categories_update = vertex[category_tab]
            all_categories.update(categories_update)

        for category in all_categories:
            vertex_subset = source_graph.vs.select(lambda node:  category in node[category_tab])
            subgraph = source_graph.induced_subgraph(vertex_subset)
        
            # Add subgraphs to generator
            yield category, subgraph

def accumulate_categories_preserved(source_graph: ig.Graph, category_tab: str) -> Generator[Tuple[str, ig.Graph], None, None]:
    
    def inheritance_connection(conn: np.ndarray, nodes: List[int]):
        n = conn.shape[0]
        
        # Create a mask to remove rows and columns of eliminated nodes
        mask = np.ones((n,), dtype=bool)
        mask[nodes] = False
        
        # Compute updates for all nodes to be eliminated
        updates = np.zeros((n, n))
        for node in nodes:
            updates += np.outer(conn[:, node], conn[node, :])
        
        # Update connections to the predecessors of the eliminated nodes
        heir = conn + updates
        
        # Remove connections from the eliminated nodes
        heir = heir[mask, :]
        heir = heir[:, mask]
        
        return heir

        

    # Obtén todas las categorías de nivel superior únicas en el grafo
    all_categories = set()
    for vertex in source_graph.vs:
        categories_update = vertex[category_tab]
        all_categories.update(categories_update)
    

    # Connection matrices
    SIZE = len(source_graph.vs.indices)
    connections = np.zeros((SIZE, SIZE), dtype=bool)
    # Add connections
    for edge in source_graph.es:
        source = edge.source
        target = edge.target

        connections[source, target] = True

    for category in all_categories:
        print("Creating subgraph,", category)
        cat_graph = source_graph.copy()
        cat_graph.delete_edges(cat_graph.es)  # Clear edges

        cat_connections = np.copy(connections)

        # Vertex delete
        vertices_to_delete = list()
        for vertex in cat_graph.vs:
            id = vertex.index
            if (vertex["type"] == "theorem") and (category not in vertex[category_tab]):
                vertices_to_delete.append(id)
        cat_connections = inheritance_connection(cat_connections, vertices_to_delete)        
        cat_graph.delete_vertices(vertices_to_delete)

        # Add connections
        true_indices = zip(*cat_connections.nonzero())

        for relation in true_indices:
            cat_graph.add_edge(*relation)

        # Iterate over the True values using the extracted indices
        cat_graph.add_edges = [(true_indices[0, i], true_indices[1, i]) for i in range(SIZE)]

        # Add subgraphs to generator
        yield category, cat_graph

