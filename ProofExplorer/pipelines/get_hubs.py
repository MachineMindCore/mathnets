from ProofExplorer.models.references import GraphReference
from ProofExplorer.functions.filters import hubs_filter

# Raw data
NATURALPROOFS_PROOFWIKI = GraphReference("data/raw/naturalproofs_proofwiki")

# Experimental data
PROOFWIKI = GraphReference("data/processed/proofwiki")

PROOFWIKI_HUBS = GraphReference("data/processed/proofwiki_hubs")
PROOFWIKI_HUBS_NEIGHBOURS = GraphReference("data/processed/proofwiki_hubs_neighbours")
hubs_filter