import json
import igraph as ig

from typing import List, Dict
from naturalproofs_toolkit.containers import GraphContainer
from naturalproofs_toolkit.functions import remove_isolated_nodes, replace_none, accumulate_top_categories


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

def build_naturalproofs(graph_addr: str) -> ig.Graph:
    """
    Build a naturalproofs dataset as graph
    """
    # Raw data
    with open(graph_addr, "r") as naturalproofs_json:
        data = json.load(naturalproofs_json)
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

    
    return new_graph

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

def build_pipeline():

    # Addresses    
    NATURALPROOF_PROOFWIKI_ADDR = "download/naturalproofs_proofwiki.json"
    PROOFWIKI_ADDR = "data/base/proofwiki"

    # Pre-building from json
    print("----> Building base from json")
    raw_proofwiki = build_naturalproofs(NATURALPROOF_PROOFWIKI_ADDR)
    proofwiki = replace_none(remove_isolated_nodes(raw_proofwiki))

    container = GraphContainer(PROOFWIKI_ADDR)
    container.seed(proofwiki)
    container.build("view")
    container.build("dist")
    container.build("sum")

    # Top categories
    print("----> Building top_categories from base")
    proofwiki_container = GraphContainer(PROOFWIKI_ADDR)
    proofwiki_graph = proofwiki_container.load()
    category_generator = accumulate_top_categories(proofwiki_graph)

    for category, subgraph in category_generator:
        print(f"Creating category: {category}")
        category_container = GraphContainer(f"data/top_categories/proofwiki_{category}")
        category_container.seed(subgraph)
        category_container.build("view")
        category_container.build("dist")
        category_container.build("sum")
