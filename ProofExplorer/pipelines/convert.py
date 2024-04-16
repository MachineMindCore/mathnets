import argparse
import igraph as ig
from ProofExplorer.models.references import GraphReference

def convert_graphs(input_addr: str, output_addr: str) -> None:
    input = ig.read(input_addr)
    ig.write(input, output_addr, format=output_addr.split(".")[-1])
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert graphs in a folder to a specified format")
    parser.add_argument("--graph", dest="graph_addr", type=str, help="Folder containing graphs in multiple formats", required=True)
    parser.add_argument("--from", dest="input_format", type=str, help="Input format (e.g., graphml, gml, net)", required=True)
    parser.add_argument("--to", dest="output_format", type=str, help="Output format (e.g., graphml, gml, net)", required=True)
    args = parser.parse_args()

    reference = GraphReference(args.graph_addr)
    reference.add(args.output_format) 
    convert_graphs(reference[args.input_format], reference[args.output_format])