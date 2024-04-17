import igraph as ig
import os

from ProofExplorer.functions.measures import generate_graph_data, generate_distribution_plots
from ProofExplorer.models import references
from ProofExplorer.models.references import GraphReference

if __name__ == "__main__":
    containers_path = "data/processed"
    for folder in os.listdir(containers_path):
        reference = os.path.join(containers_path, folder)
        container_ref = GraphReference(reference)
        print(container_ref.folder_address)
        container_graph = ig.read(container_ref["pickle"])
        container_ref.add("png")
        container_ref.add("txt")

        graph_fig = generate_distribution_plots(container_graph)
        graph_data = generate_graph_data(container_graph, name=container_ref.name)

        graph_fig.savefig(container_ref["png"])
        with open(container_ref["txt"], 'w') as data_file:
            data_file.write(graph_data)

