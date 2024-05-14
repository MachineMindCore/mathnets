from icecream import ic
from naturalproofs_toolkit.containers import GraphMachine

machine = GraphMachine("data/")

ic(machine.groups)
ic(machine.paths)
ic(machine.handlers)
