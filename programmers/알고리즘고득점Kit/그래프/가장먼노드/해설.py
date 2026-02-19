from collections import deque

def solution(n, edge):
    # 1. 인접 리스트 그래프 만들기
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)  # 양방향

    # 2. 거리 배열 초기화 (-1이면 아직 방문 안 함)
    dist = [-1] * (n + 1)
    dist[1] = 0  # 시작 노드 1의 거리는 0

    # 3. BFS
    q = deque([1])
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if dist[nx] == -1:           # 처음 방문하는 노드만
                dist[nx] = dist[x] + 1   # 현재 노드 거리 + 1
                q.append(nx)

    # 4. 1번 노드에서의 최댓거리 찾기
    max_dist = max(dist[1:])            # 0번 인덱스는 안 쓰니까 제외

    # 5. 최댓거리를 가진 노드 수 세기
    return dist[1:].count(max_dist)
