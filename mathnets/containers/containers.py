import zipfile
import warnings
import json
import os
import igraph as ig
from mathnets.functions import generate_graph_data, generate_distribution_plots, get_hubs
from typing import Any

warnings.filterwarnings("ignore")
"""
PLOT_CONFIG_BIG = {
    ""
                graph, 
            layout=layout, 
            vertex_size=0.1, 
            edge_width=0.001, 
            bbox=(1000, 1000), 
            vertex_label_size=0.1,
            arrow_size = 0.001, 
            target=plot_addr
}
"""
class GraphContainer:

    # Constructor
    def __init__(self, folder_address: str) -> None:
        self.BUILDERS = {
            "view": self._build_view,
            "dist": self._build_dist,
            "hubs": self._build_hubs,
            "sum": self._build_sum,
        }
        self.LOADERS = {
            "seed": self._load_seed, 
            "view": self._load_view,
            "dist": self._load_dist,
            "hubs": self._load_hubs,
            "sum": self._load_sum,
        }
        
        self.name = folder_address.split("/")[-1]
        self.folder_address = folder_address
        self.graph = ig.Graph()
        self._make_dirs()
        return


    # Building methods
    def seed(self, graph: ig.Graph) -> None:
        format = "pickle"
        self.graph = graph
        addr = self._make_fileaddr(format)
        plot_addr = self._make_fileaddr("pdf")
        ig.write(graph, addr, format=format)
        graph.vs['label'] = graph.vs['id']
        # Generate layout
        layout = graph.layout_auto()
        ig.plot(
            graph, 
            layout=layout, 
            vertex_size=0.1, 
            edge_width=0.001, 
            bbox=(1000, 1000), 
            vertex_label_size=0.1,
            arrow_size = 0.0001,
            arrow_width = 0.0001,
            target=plot_addr
        )
        return

    def build(self, option: str = "") -> None:
        """
        Auto building method to compose all data representing graph.
        """
        if option == "":
            for builder in self.BUILDERS.values():
                builder()
        elif option in self.BUILDERS.keys():
            self.BUILDERS[option]()
        else:
            raise ValueError("Building option not implemented")
        return

    def load(self, option: str = "") -> Any:
        """
        Auto loading method to get data representing graph
        """
        if option == "":
            load = self.LOADERS["seed"]()
        elif option in self.LOADERS.keys():
            load = self.LOADERS[option]()
        else:
            raise ValueError("Loader option not implemented")
        return load

    def package(self) -> None:
        addr = self.folder_address
        with zipfile.ZipFile(f'{self.name}.zip', 'w') as zf:
            for item in os.listdir(addr):
                full_path = os.path.join(addr, item)
                if os.path.isfile(full_path) and not full_path.endswith('.zip'):
                    zf.write(full_path, arcname=item)
        return
    
    def unpackage(self) -> None:
        return


    # Subsave IO functions
    def _build_view(self) -> None:
        format = "gml"
        addr = self._make_fileaddr(format)
        ig.write(self.graph, addr, format=format)
        return
    
    def _build_sum(self) -> None:
        format = "summarize.txt"
        summarize = generate_graph_data(self.graph, name=self.name)
        addr = self._make_fileaddr(format)
        with open(addr, 'w') as file:
            file.write(summarize)
        return
    
    def _build_dist(self) -> None:
        format = "png"
        fig = generate_distribution_plots(self.graph)
        addr = self._make_fileaddr(format)
        fig.savefig(addr)
        return
    
    def _build_hubs(self) -> None:
        format = "hubs.json"
        addr = self._make_fileaddr(format)
        hubs = get_hubs(self.graph, 10)
        with open(addr, "w") as json_file:
            json.dump(hubs, json_file, indent=4)


    # Subload IO functions
    def _load_seed(self) -> ig.Graph:
        format = "pickle"
        addr = self._make_fileaddr(format=format)
        load = ig.read(addr)
        return load
        
    def _load_view(self) -> ig.Graph:
        format = "gml"
        addr = self._make_fileaddr(format=format)
        load = ig.read(addr)
        return load
    
    def _load_dist(self):
        pass

    def _load_sum(self):
        pass

    def _load_hubs(self):
        format = "hubs.json"
        addr = self._make_fileaddr(format=format)
        file = open(addr) 
        load = json.load(file)
        file.close()
        return load


    # Helpers
    def _make_fileaddr(self, format: str) -> str:
        return f"{self.folder_address}/{self.name}.{format}"

    def _make_dirs(self) -> None:
        os.makedirs(self.folder_address, exist_ok=True)
        if self.folder_address[-1] == "/": 
            self.folder_address = self.folder_address[:-1]
        return
    