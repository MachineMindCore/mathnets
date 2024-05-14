import argparse
from naturalproofs_toolkit.pipelines import build_pipeline, roadmap_pipeline, download_pipeline

def main():
    parser = argparse.ArgumentParser(description="Description of your program")
    parser.add_argument("--download", action="store_true", help="Download something")
    parser.add_argument("--build", action="store_true", help="Build something")
    parser.add_argument("--roadmap", nargs=3, metavar=("GRAPH_ADDR", "FROM_ID", "TO_ID"), help="Roadmap description")

    args = parser.parse_args()

    if args.download:
        download_pipeline()
    if args.build:
        build_pipeline()
    if args.roadmap:
        graph_addr, from_id, to_id = args.roadmap
        roadmap_pipeline(graph_addr, from_id, to_id)
        print(f"Roadmap: {graph_addr} | from {int(from_id)} to {int(to_id)}")

if __name__ == "__main__":
    main()