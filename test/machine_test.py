from icecream import ic
from mathnets.containers import GraphMachine

machine = GraphMachine("data/")

ic(machine.groups)
ic(machine.paths)
ic(machine.handlers)
