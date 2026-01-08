from collections import deque

# 너비 우선 탐색
def bfs(start, graph, n):
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

# 깊이 우선 탐색
def dfs(node, graph, visited):
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt, graph, visited)

# 파보나치 수열
def fibonacci_sequence(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

print(fibonacci_sequence(10))

def is_primary(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True