import igraph as ig
import subprocess
from ProofExplorer.models.references import GraphReference
from ProofExplorer.functions.acumulations import accumulate_categories, accumulate_categories_isolated

CONVERT_SCRIPT = "ProofExplorer/pipelines/convert.py"
STATTICAL_ARGS = ['--from', 'pickle', '--to', 'gml']

if __name__ == "__main__":
    PROOFWIKI_REF = GraphReference("data/processed/proofwiki")
    proofwiki = ig.read(PROOFWIKI_REF["pickle"])
    category_generator = accumulate_categories_isolated(proofwiki, "toplevel_categories")

    for category, subgraph in category_generator:
        print(f"Creating category: {category}")
        temp_ref = GraphReference(f"data/isolated_categories/proofwiki_{category}")
        temp_ref.add("pickle")
        temp_ref.add("gml")

        subgraph.write(temp_ref["pickle"], format="pickle")

        dinamic_arg = ["--graph", temp_ref.folder_address]
        args = dinamic_arg + STATTICAL_ARGS

        command = ['python3', CONVERT_SCRIPT] + args

        # Ejecuta el comando
        subprocess.run(command)
