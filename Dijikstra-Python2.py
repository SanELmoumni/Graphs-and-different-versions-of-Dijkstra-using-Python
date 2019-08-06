from collections import defaultdict, OrderedDict
from heapq import *
 
def ugraph(*edges):
    G = defaultdict(dict)
    for src,dst,cost in edges:
        G[src][dst] = cost
        G[dst][src] = cost
    return G
 
def dijkstra(G, v):
    candidates = [(0,v,None)]   # (total cost, current node, previous node)
    result = OrderedDict()
    while candidates:
        cost,curr,prev = heappop(candidates)
        if curr in result: continue
        result[curr] = (prev, cost)
        for next in G[curr].keys():
            if next not in result:
                heappush(candidates, (cost + G[curr][next],next,curr))
    return result
 
if __name__ == '__main__':
    net = ugraph(
        ('A','B',5) , ('A','C',5) , ('A','D',20),
        ('B','C',5) , ('B','E',10),
        ('C','D',10), ('C','F',8) , ('C','G',10), ('C','H',6),
        ('D','F',6) ,
        ('E','H',7) ,
        ('F','K',7) ,
        ('G','H',6) , ('G','J',8),
        ('H','I',20),
        ('I','J',5) ,
        ('J','K',6) ,
        ('K','L',20), ('K','M',5),
        ('L','M',5)
        )
 
    path = dijkstra(net, 'A')
    print(path)