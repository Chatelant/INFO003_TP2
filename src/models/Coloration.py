from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    NULL = -1


class Coloration:
    def __init__(self, nodes):
        self.nodes = nodes
    
    def __str__(self):
        res = ""
        for color in self.nodes:
            res += f"[{color}] "
        return res
