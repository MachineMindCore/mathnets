import argparse
import igraph as ig
from ProofExplorer.models.references import GraphReference
from ProofExplorer.functions.filters import k_core_graph

if __name__ == "__main__":
    proofwiki_ref = GraphReference("data/processed/proofwiki_A")
    kcore7_ref = GraphReference("data/processed/proofwiki_kcore7")

    proofwiki = ig.read(proofwiki_ref["pickle"])
    kcore7 = k_core_graph(proofwiki, 10)

    kcore7_ref.add("pickle")
    kcore7.write(kcore7_ref["pickle"], format="pickle")




