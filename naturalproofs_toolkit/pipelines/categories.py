from naturalproofs_toolkit.containers.containers import GraphContainer
from naturalproofs_toolkit.functions.multiplexers import accumulate_top_categories

def categories_pipeline():

    PROOFWIKI_ADDR = "data/base/proofwiki"
    proofwiki_container = GraphContainer(PROOFWIKI_ADDR)
    proofwiki_graph = proofwiki_container.load()
    category_generator = accumulate_top_categories(proofwiki_graph, "toplevel_categories")

    for category, subgraph in category_generator:
        print(f"Creating category: {category}")
        category_container = GraphContainer(f"data/top_categories/proofwiki_{category}")
        category_container.seed(subgraph)
        category_container.build()
