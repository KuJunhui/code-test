from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)
    for parent, child in edge:
        graph[parent].append(child)
    # print(graph)
    for parent, child in edge:
        graph[child].append(parent)
    # print(graph)

    node_distance = [0] * (n + 1)

    # BFS
    def bfs(node, graph):
        q = deque()
        q.append((1, 0))
        visited = [False] * (n + 1)
        visited[1] = True
        while q:
            node, distance = q.popleft()
            node_distance[node] = distance

            for nxt_node in graph[node]:
                if not visited[nxt_node]:
                    visited[nxt_node] = True
                    q.append((nxt_node, distance + 1))

    bfs(1, graph)
    # print(node_distance)
    # print(node_distance.count(max(node_distance)))

    return node_distance.count(max(node_distance))