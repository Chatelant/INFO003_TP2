# coding=utf-8

from sys import argv
from random import randint

seen = set()
def gencoordinates(s):
    x = randint(1, s-1)
    y = randint(x+1, s)
    while (x, y) in seen:
        x = randint(1, s-1)
        y = randint(x+1, s)
    seen.add((x, y))
    yield (x, y)



def main(s, filename):
    n_edges = min(randint(s, (s**2)//4), (s*(s-1))//2)
    with open(filename,'w') as file:
        file.write("Graph{\n")
        file.write("s1")
        for i in range(2,s+1):
            file.write(" s"+str(i))
        for i in range(n_edges):
            x,y = next(gencoordinates(s))
            file.write("\ns"+str(x)+"-s"+str(y))
        file.write("\n}")



if __name__ == '__main__':
    if len(argv) <= 2 and not argv[1].isdigit():
        print("La fonction attend en argument la taille du graphe demandé puis le nom du fichier à écrire.")
    elif int(argv[1]) <= 1:
        print('Le graphe doit être de taille au moins 2.')
    else:
        main(int(argv[1]),argv[2])