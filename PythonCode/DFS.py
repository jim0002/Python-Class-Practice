graph = {

    '0': ['1', '3'],

    '1': ['3', '2', '5', '6'],

    '2': ['3', '1', '5', '4'],

    '3': ['1', '2', '4'],

    '4': ['3', '2', '6'],

    '5': ['1', '2'],

    '6': ['1', '4']

}

visited = set()

def dfs(graph, visited, node):

  if node not in visited:

    print(node)

    visited.add(node)

    for adjacent in graph[node]:

      dfs(graph, visited, adjacent)



print("Graph in depth first search: ")

dfs(graph, visited, '0')