"""
This script clean data from naturalproofs raw file (only proofwiki).

Criteria:
    - Unconnected nodes
    - Unconnected graphs to main graph
"""
import igraph as ig
from ProofExplorer.models.references import GraphReference
from ProofExplorer.functions.filters import unconnected_filter

# Raw NaturalProofs (proofwiki)
NATURALPROOF_PROOFWIKI = GraphReference("data/raw/naturalproofs_proofwiki")

# Cleaned NaturalProofs (proofwiki)
PROOFWIKI = GraphReference("data/processed/proofwiki")

if __name__ == "__main__":
    raw_graph = ig.read(NATURALPROOF_PROOFWIKI["pickle"])
    proofwiki_graph = unconnected_filter(raw_graph)
    PROOFWIKI.add("pickle")
    ig.write(proofwiki_graph, PROOFWIKI["pickle"])
    
