# coding=utf-8

import sys
from pycosat import solve as solveSAT

from models.Graph import Graph


def counter(l_literals, val, new_var):
    """
    Contraintes de comptage
    Retourne les contraintes pour assurer qu'exactement `val' 
    litéraux de `l_literals' soient vrais.
    `new_var' est un indice à partir duquel les variables sont 
    neuves.
    -solveSAT(counter([1,2,3],2,4)) retourne
    Solution for SAT
    [-1, 2, 3, -4, -5, 6, -7, -8, 9]
    """

    """
    Nouvelles variables s[i,j] : au moins j des i premières variables sont vraies
    1 <= j <= val
    1 <= i <= len(L_literals)
    j <= i
    """
    n = len(l_literals)

    if val > n:  # Si val>n, on retourne deux clauses contradictoires
        return [[new_var], [-new_var]]

    s = {}
    l_output = []

    s[(1, 1)] = l_literals[0]  # s[1,1] == l_literals[0]

    acc = new_var
    for i in range(2, n + 1):  # Cas limite où j==1
        s[(i, 1)] = acc
        acc += 1
        l_output.append([-s[(i, 1)], l_literals[i - 1], s[i - 1, 1]])

    for j in range(2, val + 1):
        s[(j, j)] = acc  # Cas limite où i==j
        acc += 1
        l_output.append([-s[(j, j)], s[j - 1, j - 1]])
        l_output.append([-s[(j, j)], l_literals[j - 1]])

        for i in range(j + 1, n + 1):  # Cas général
            s[(i, j)] = acc
            acc += 1
            l_output.append([-s[(i, j)], s[i - 1, j], s[i - 1, j - 1]])
            l_output.append([-s[(i, j)], s[i - 1, j], l_literals[i - 1]])

    l_output.append([s[(n, val)]])
    return l_output


def solveClique(g, size, versatile):
    """
    Résout le problème Clique
    :param g: graphe G
    :param size: taille de la clique recherchée
    :return: cherche s'il existe une clique de taille 
    `size' dans G.
    """

    ####  La suite est à compléter/modifier (décommentez petit à petit les lignes commençant par #)

    n = len(g.nodes) # nombre de noeuds du graphe

    """ 
    Nos variables seront X1, ..., Xn
    """

    nodes = []
    for i in range(1, n + 1):
        nodes.append(i)

    """
    On veut que la clique soit de taille `size'.
    Donc parmi les n variables X1, ..., Xn, exactement `size' doivent être vraies.
    Déjà n variables sont utilisées, donc les nouvelles variables commenceront à n+1.
    """
    cnf = counter(nodes, size, n+1)
    
    """
    Pour chaque paire de sommets (u, v), si (u, v) n'est pas une arête, on rajoute 
    la contrainte qu'une des extrémités ne doit pas appartenir à la clique.
    """
    for u in range(1, n + 1): 
        for v in range(1, u):
            if v not in g.nodes[u - 1]:
                cnf.append([-u, -v])

    if versatile:
        print("Entrée pour le SAT solveur")
        print(cnf)

    return cnf


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage : python3 solveClique.py <filename> <size_clique>")
        exit(1)
    filename = sys.argv[1]
    try:
        size = int(sys.argv[2])
    except:
        print("Le deuxième argument <size_clique> doit être un entier.")
        exit(1)
    if len(sys.argv) > 3 and (sys.argv[3] == "-v" or sys.argv[3] == "--versatile"):
        versatile = True
    else:
        versatile = False

    ######## Récupérer le graphe stocké dans le fichier <filename>
    g = Graph(filename)

    ######## Si c'est possible pour votre structure de données, vous pouvez afficher le graphe
    if versatile:
        print("Graphe d'entrée")
        print(g)

    solution = solveClique(g, size, versatile)
    result = solveSAT(solution)

    if versatile:
        print("Solution pour SAT")
        print(result)
    print("Solution pour le problème Clique")
    if result != "UNSAT":
        print([i for i in result[:len(g.nodes)] if i > 0])
    else:
        print("Pas de clique de taille " + str(size) + ".")
