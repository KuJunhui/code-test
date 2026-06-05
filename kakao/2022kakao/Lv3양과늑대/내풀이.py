from collections import defaultdict

def solution(info, edges):
    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)

    return dfs(0, 0, 0, [0], info, graph)

def dfs(node, sheep, wolf, available, info, graph):
    if info[node] == 0:
        sheep += 1
    else:
        wolf += 1

    if wolf >= sheep:
        return sheep - 1

    next_nodes = available.copy()
    next_nodes.remove(node)
    next_nodes.extend(graph[node])

    max_sheep = sheep
    for next_node in next_nodes:
        max_sheep = max(max_sheep, dfs(next_node, sheep, wolf, next_nodes, info, graph))
    return max_sheep

