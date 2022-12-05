import copy
import random
from models.Coloration import Coloration, Color
from models.Graph import Graph


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
        # Recuperation de la couleur courante
        colorCurr = coloration.nodes[node]
        
        # Pour chaques voisins
        for neigbour in graph.nodes[node]:
            
            # On considère que la présence d'une chaine de caractère vide est valide
            if coloration.nodes[neigbour -1] == '':
                break
                
            # Si la coloration est la même que le noeud courant
            if coloration.nodes[neigbour - 1] == colorCurr or colorCurr == Color.NULL:
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
    coloration = initColoration(graph)
    return genColoration(graph, coloration, 0)


# -------------------- Question 3 -------------------- #
# Retourne la couleur suivante à tester
def nextColor(color: Color):
    if color == '':
        return Color.RED
    elif color == Color.RED:
        return Color.GREEN
    elif color == Color.GREEN:
        return Color.BLUE
    elif color == Color.BLUE:
        return Color.NULL

# Fonction récursive
def solvBackTrackingRec(graph, color, index):
    while color.nodes[index] != Color.NULL:
        color.nodes[index] = nextColor(color.nodes[index])
        if verificateur(graph, color):
            if(index == len(graph.nodes) - 1):
                return True
            if(solvBackTrackingRec(graph,color, index + 1)):
                return True
    color.nodes[index] = ''
    return False

# Fonction principale
def solvBackTracking(graph: Graph):
    currIndex = 0
    coloration = initColoration(graph)
    solvBackTrackingRec(graph, coloration, currIndex)
    return coloration

# -------------------- Question 4 -------------------- #
# Retourne une couleur aléatoire
def getRandomColor():
    rand = random.randrange(0,3)
    if(rand == 0): return Color.RED
    elif(rand == 1): return Color.GREEN
    else: return Color.BLUE

# Indique si un noeud est problématique
def estProblematique(graph : Graph, colors : Color, index : int):
    currColor = colors.nodes[index]
    neigbour = graph.nodes[index]
    for node in neigbour:
        if colors.nodes[node - 1] == currColor:
            return True
    return False

# Retourne la liste des noeuds problématiques
def sontProblematique(graph : Graph, colors : Color):
    nodesProblematiques = []
    for iNode in range(len(graph.nodes)):
        if(estProblematique(graph, colors,iNode)):
            nodesProblematiques.append(iNode)
    return nodesProblematiques

def solvHeuristique(graph : Graph):
    # Initialisation
    colors = initColoration(graph)
    for iNode in range(len(colors.nodes)):
        colors.nodes[iNode] = getRandomColor()
    
    # Arretes problematiques
    nodesProblematiques = sontProblematique(graph, colors)
    k = len(nodesProblematiques)
    
    compt = 100
    while compt > 0:
        index = random.randrange(0,len(nodesProblematiques))    
        colors.nodes[index] = getRandomColor()
        nodesProblematiques = sontProblematique(graph, colors)
        k = len(nodesProblematiques)
        if k == 0 : 
            return colors
        compt -= 1
        
    return initColoration(graph)    
    


if __name__ == "__main__":
    # Création graph
    graph = Graph('exemples/3C_vrai20.txt')
    # print(graph)

    # Coloration
    # colorationMain = Coloration([Color.RED, Color.GREEN, Color.BLUE, Color.BLUE])

    # Verification du graph d'entrée (Q1)
    # print(verificateur(graph, colorationMain))S

    # Verification de toutes les possibilitées (Q2)
    # print(genereEtTeste(graph))
    
    # Backtracking (Q3)
    # print(f"Question 3 -> {solvBackTracking(graph)}")

    # Heuristique (Q4)
    # print(f"Question 4 -> {solvHeuristique(graph)}") # Trouve que tres rarement