from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    NULL = -1


class Coloration:
    def __init__(self, nodes: [Color]):
        self.nodes = nodes
