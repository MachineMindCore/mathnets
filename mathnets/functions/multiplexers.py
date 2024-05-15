"""
GROUP TRANSFORMATIONS FUNTIONS

# Structure
(generator) function(graph: Graph, **kwargs) -> tag: str, subgraph: Graph
"""
import igraph as ig
from typing import Generator

def accumulate_top_categories(source_graph: ig.Graph, **kwargs) -> Generator[tuple, None, None]:       
      def get_categories(graph: ig.Graph) -> set:
            all_categories = set()
            for vertex in graph.vs:
                  categories_update = vertex["toplevel_categories"]
                  all_categories.update(categories_update)
            return all_categories
      
      # Obtén todas las categorías de nivel superior únicas en el grafo
      all_categories = get_categories(source_graph)
      for category in all_categories:
            vertex_subset = source_graph.vs.select(lambda node: (node["type"] in ["definition", "other"]) or (category in node["toplevel_categories"]))
            subgraph = source_graph.induced_subgraph(vertex_subset)

            # Add subgraphs to generator
            yield category, subgraph
            
