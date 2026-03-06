from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1] * (n + 1)
    distance[1] = 0
    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        for nxt_node in graph[node]:
            if distance[nxt_node] == -1:
                distance[nxt_node] = distance[node] + 1
                q.append(nxt_node)

    return distance.count(max(distance))
