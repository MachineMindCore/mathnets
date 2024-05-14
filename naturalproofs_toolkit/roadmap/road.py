import igraph as ig

def map_id(graph: ig.Graph, original_id: int):
    return graph.vs.select(lambda x: x["id"] == original_id)[0].index

def demap_id(graph: ig.Graph, mask_id: int):
    return graph.vs(mask_id)[0]["id"]

def make_roadmap(graph: ig.Graph, from_id: int, to_id: int) -> ig.Graph:
    graph = graph.as_undirected()
    subgraph = ig.Graph()

    # Find the shortest path from node_a to node_b
    shortest_indices = set()
    mapped_from_id = map_id(graph, from_id)
    mapped_to_id = map_id(graph, to_id)
    shortest_collection = graph.get_all_shortest_paths(mapped_from_id, to=mapped_to_id, mode="out")

    for short_path in shortest_collection:
        for idx in short_path:
            shortest_indices.add(idx)
    shortest_indices = list(shortest_indices)
    subgraph.add_vertices(shortest_indices, attributes={"id": shortest_indices})
    index_dict = dict(zip(shortest_indices, subgraph.vs.indices))

    for node_A in shortest_indices:
        for node_B in shortest_indices:
            if graph.are_connected(node_A, node_B):
                subgraph.add_edge(index_dict[node_A], index_dict[node_B])

    # Copy over attributes from the original graph to the subgraph
    for attr in graph.vs.attributes():
        subgraph.vs[attr] = graph.vs(shortest_indices)[attr]

    return subgraph
