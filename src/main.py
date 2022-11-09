import copy

from src.models.Coloration import Coloration, Color
from src.models.Graph import Graph

# ----- Utils ----- #
def initColoration(graph : Graph):
    coloration = Coloration([])
    for i in range(len(graph.nodes)):
        coloration.nodes.append('')
    return coloration

# -------------------- Question 1 -------------------- #
# Vérifie si le graph est 3-coloriable avec la coloration donnée
def verificateur(graph: Graph, coloration: Coloration):
    for node in range(len(graph.nodes)):
        colorCurr = coloration.nodes[node]
        for neigbour in graph.nodes[node]:
            if coloration.nodes[neigbour - 1] == colorCurr:
                return False
    return True


# -------------------- Question 2 -------------------- #

# Fonction recursive crée l'ensemble des colorations possibles pour un graph et les test
# Return true si le graph est 3-colorable
# Est call dans genereEtTeste
def genColoration(graph: Graph, coloration: Coloration, indice: int):
    blue: Coloration = copy.deepcopy(coloration)
    red: Coloration = copy.deepcopy(coloration)
    green: Coloration = copy.deepcopy(coloration)

    blue.nodes[indice] = Color.BLUE
    red.nodes[indice] = Color.RED
    green.nodes[indice] = Color.GREEN

    if indice == len(coloration.nodes) - 1:
        return verificateur(graph, blue) or verificateur(graph, red) or verificateur(graph, green)
    else:
        return genColoration(graph, blue, indice + 1) \
               or genColoration(graph, green, indice + 1) \
               or genColoration(graph, red, indice + 1)


# Genere toutes les combinaisons possibles de colorations pour le graph
# et test pour chacune jusqu'à ce qu'on trouve une 3-coloration ou
# qu'il n'y en ait aucune possible
def genereEtTeste(graph: Graph):
    coloration =initColoration(graph)
    return genColoration(graph, coloration, 0)


# -------------------- Question 3 -------------------- #
# Retourne la couleur suivante à tester
def nextColor(color: Color):
    if color == Color.RED:
        return Color.GREEN
    elif color == Color.GREEN:
        return Color.BLUE
    else:
        return Color.NULL


def solvBackTracking(graph: Graph):
    currIndex = 0
    coloration = initColoration(graph)
    pass


if __name__ == "__main__":
    # Création graph
    graph = Graph('exemples/3C_vrai.txt')

    # Coloration
    coloration = Coloration([Color.BLUE, Color.GREEN, Color.RED, Color.RED])

    # Verification du graph d'entrée
    # print(verificateur(graph, coloration))

    # Verification de toutes les possibilitées
    print(genereEtTeste(graph))
