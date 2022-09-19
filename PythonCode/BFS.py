graph= {2: [0,3], 0: [1,2], 1: [2], 3: [3]}
discovered=[]
queue=[]
def bfs (discovered,graph,node):
    discovered.append(node)
    queue.append(node)

    while queue:
        g=queue.pop(0)
        print(g)
        for child in graph[g]:
            if child not in discovered:
                discovered.append(child)
                queue.append(child)
print('BFS : ')
bfs(discovered,graph,2)