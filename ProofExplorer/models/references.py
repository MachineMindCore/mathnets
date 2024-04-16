import os
import glob
from pathlib import Path

class GraphReference:
    def __init__(self, folder_address: str) -> None:
        os.makedirs(folder_address, exist_ok=True)
        if folder_address[-1] == "/": 
            folder_address = folder_address[:-1]

        self.name = folder_address.split("/")[-1]
        self.folder_address = folder_address
        self.graphs_formats = set()
        self._find_graphs()
        return
    
    def __getitem__(self, format: str) -> str:
        if format not in self.graphs_formats:
            raise Exception(f"Not {format} format found in folder container")
        return f"{self.folder_address}/{self.name}.{format}"
    
    def _find_graphs(self) -> None:
        folder_path = self.folder_address
        match_string = self.name
        files = glob.glob(os.path.join(folder_path, "*"))

        for file in files:
            filename = os.path.basename(file)
            if match_string in filename:
                file_format = filename.split(".")[-1]
                self.graphs_formats.add(file_format)
        return
    
    def add(self, graph_format: str) -> None:
        Path(f"{self.folder_address}/{self.name}.{graph_format}").touch()
        self.graphs_formats.add(graph_format)
        return