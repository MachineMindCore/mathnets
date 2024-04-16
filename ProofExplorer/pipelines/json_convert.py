import json
import sys
import igraph as ig

from typing import List, Dict

GRAPH_FORMAT = sys.argv[1]

def add_type(collection: List[dict], math_type: str) -> List[dict]:
    """

    Add type variable (one by one) to a list of nodes.
    Args:
        collection (List[dict]): List of nodes
        math_type (str): Type or classification of node

    Returns:
        collection (List[dict]): List of nodes modificated
    """
    for item in collection:
        item["type"] = math_type
    return collection

def create_netdata(node_data):
    STANDARD_TYPES = (int, float, str, bool)
    standard_data = dict()
    
    for key, value in node_data.items():
        if isinstance(value, dict):
            standard_data[key]
        elif key == "proofs":
            for i, proof in enumerate(value):
                for proof_key, proof_value in proof.items():
                    subkey = f"{proof_key}_proof-{i}"
                    if isinstance(proof_value, list):
                        standard_data[subkey] = '\n'.join(str(subvalue) for subvalue in proof_value)
                    standard_data[subkey] = proof_value
        elif isinstance(value, list):
            standard_data[key] = '\n'.join(str(subvalue) for subvalue in value)
        elif isinstance(value, STANDARD_TYPES):
            standard_data[key] = value
        else:
            raise Exception(f"Some node item have invalid type: {value}")
    return standard_data

def load_naturalproofs(graphs: Dict[dict, dict]):
    """
    Args:
        graphs (Dict[dict, dict]): _description_

    Returns:
        _type_: _description_
    """
    for graph_name in graphs.keys():
        with open(graphs[graph_name]["address"], 'r') as f:
            
            # Raw data
            data = json.load(f)
            new_graph = ig.Graph(directed=True)

            # Data extraction
            theorems = data["dataset"]["theorems"]
            definitions = data["dataset"]["definitions"]
            others = data["dataset"]["others"]
            
            # Graph data
            graph_data = add_type(theorems, "theorem") + add_type(definitions, "definition") + add_type(others, "other")
            
            # Vertex creation
            edges = []
            for raw_data in graph_data:
                node_data = raw_data
                node_id = int(node_data["id"])
                # Edge creation
                for ref in node_data["ref_ids"]:
                    if isinstance(ref, int):
                        edges.append((node_id, int(ref)))
                new_graph.add_vertex(name=str(node_id), **node_data)
            new_graph.add_edges(edges)

            # Save graph
            graphs[graph_name]["content"] = new_graph

    return graphs

def save_graphs(graphs: Dict[dict, dict], graph_format: str):
    """_summary_

    Args:
        graphs (Dict[dict, dict]): _description_
        graph_format (str): _description_

    Returns:
        _type_: _description_
    """
    for graph_name in graphs.keys():
        save_address = graphs[graph_name]["address"].split(".")[0]
        graphs[graph_name]["content"].write(f"{save_address}.{graph_format}", format=graph_format)
    return None

if __name__ == "__main__":
    # Create a new graph
    structure = {
        "proofwiki": {
            "content": ig.Graph(),
            "address": "data/naturalproofs_proofwiki/naturalproofs_proofwiki.json"
        },
        "stacks": {
            "content": ig.Graph(),
            "address": "data/naturalproofs_stacks/naturalproofs_stacks.json"
        },
        "stein": {
            "content": ig.Graph(),
            "address": "data/naturalproofs_stein/naturalproofs_stein.json"
        },
        "trench": {
            "content": ig.Graph(),
            "address": "data/naturalproofs_trench/naturalproofs_trench.json"
        }
    }

    loaded_graphs = load_naturalproofs(structure)
    save_graphs(loaded_graphs, graph_format=GRAPH_FORMAT)

    # Summary
    print("------------- Graph format convertion -------------")
    print(f"Saved format: {GRAPH_FORMAT}")
    for graph_name, metadata in loaded_graphs.items():
        print(f"GRAPH ---> {graph_name}")
        ig.summary(metadata["content"])
        