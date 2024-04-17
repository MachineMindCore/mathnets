from igraph import Graph
from typing import Set

def get_categories(graph: Graph) -> Set[str]:
    all_categories = set()
    for vertex in source_graph.vs:
        categories_update = vertex[category_tab]
        all_categories.update(categories_update)
    return all_categories