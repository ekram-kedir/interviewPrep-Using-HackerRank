from collections import defaultdict
edge = defaultdict(list)

def AddEdge(u , v):
    edge[u].append(v)
    edge[v].append(u)

def Vertex(u):
    print(*edge[u])

length = int(input())
tasks = int(input())

for task in range(tasks):
    values = list(map(int,input().split()))
    if values[0] == 1:
        AddEdge(values[1], values[2])
    else:
        Vertex(values[1])
