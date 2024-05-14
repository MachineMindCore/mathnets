"""
This script clean data from naturalproofs raw file (only proofwiki).

Criteria:
    - Unconnected nodes
    - Unconnected graphs to main graph
"""
import igraph as ig
from naturalproofs_toolkit.containers.containers import GraphReference
from naturalproofs_toolkit.functions.transformations import remove_isolated_nodes, replace_none

# Raw NaturalProofs (proofwiki)
NATURALPROOF_PROOFWIKI = GraphReference("data/raw/naturalproofs_proofwiki")

# Cleaned NaturalProofs (proofwiki)
PROOFWIKI = GraphReference("data/processed/proofwiki")

if __name__ == "__main__":
    raw_graph = ig.read(NATURALPROOF_PROOFWIKI["pickle"])
    proofwiki_graph = replace_none(remove_isolated_nodes(raw_graph), replace_item=[])
    PROOFWIKI.add("pickle")
    ig.write(proofwiki_graph, PROOFWIKI["pickle"])
    
