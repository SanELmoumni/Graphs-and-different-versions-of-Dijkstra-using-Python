# coding: utf-8

# La biblioth�que standard "heapq" fournit les fonctions de manipulation d'un
# tas: juste ce qu'il nous faut pour impl�menter la file des sommets � traiter.

from heapq import *

# Impl�mentation de l'algorithme de Dijkstra en Python.
#
# Les arguments sont:
#  - s : le sommet source
#  - t : le sommet but
#  - voisins : fonction qui pour un sommet renvoie une liste de couples
#      (poids, sommet) pour chaque ar�te sortante
# Les sommets doivent �tre des objets "hachables" (nombres, cha�nes de
# caract�res, n-uplets...).

def dijkstra (s, t, voisins):
    M = set()
    d = {s: 0}
    p = {}
    suivants = [(0, s)] # tas de couples (d[x],x)

    while suivants != []:

        dx, x = heappop(suivants)
        if x in M:
            continue

        M.add(x)

        for w, y in voisins(x):
            if y in M:
                continue
            dy = dx + w
            if y not in d or d[y] > dy:
                d[y] = dy
                heappush(suivants, (dy, y))
                p[y] = x

    path = [t]
    x = t
    while x != s:
        x = p[x]
        path.insert(0, x)

    return d[t], path


# Exemple d'utilisation avec un graphe repr�sent� par une liste d'adjacence.

graph = {
    "A": [ (27, "D"), (2, "G") ],
    "B": [ (1, "A") ],
    "C": [ (1, "B"), (2, "F"), (3, "G") ],
    "D": [ (4, "G"), (7, "H") ],
    "E": [ (5, "A"), (3, "B"), (2, "C") ],
    "F": [ (8, "H"), (1, "D") ],
    "G": [ (4, "F") ],
    "H": []
}

def voisins (s):
    return graph[s]