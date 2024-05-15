from mathnets.containers import GraphContainer
from mathnets.roadmap import RoadMapper

def decode_ids(graph_addr: str, encoded_ids: str):
    codes = encoded_ids.split("-")
    graph_container = GraphContainer(graph_addr)
    from_ids = list()
    for code in codes:
        if code.isnumeric():
            id = int(code)
            from_ids.append(id)
        elif code[0] == "h":
            hub_id = int(code[1:])
            hubs = graph_container.load("hubs")
            id = int(list(hubs.keys())[hub_id])
            from_ids.append(id)
        elif code == "H":
            hubs = graph_container.load("hubs")
            from_ids = list(map(int, hubs.keys()))
            break
        else:
            raise ValueError("Wrong code input")
        from_ids.append(id)
    
    return from_ids

def roadmap_pipeline(graph_addr: str, from_code: str, to_id: int):
    roadmapper = RoadMapper(graph_addr)
    from_ids = decode_ids(graph_addr, from_code)
    roadmapper.map(from_ids, to_id)


"""
def _roadmap_pipeline(graph_addr: str, encodings: list):
    for encoded_ids in encodings:
    roadmapper = RoadMapper(graph_addr)
    from_ids = decode_ids(from_code)
    roadmapper.map(from_ids, to_id)
"""