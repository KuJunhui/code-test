def solution(n, computers):
    visited = [False] * n   # 각 컴퓨터 방문 여부
    answer = 0

    def dfs(node):
        visited[node] = True
        for next_node in range(n):
            # 연결되어 있고, 아직 방문 안 했으면 계속 타고 들어감
            if computers[node][next_node] == 1 and not visited[next_node]:
                dfs(next_node)

    for i in range(n):
        # 아직 방문 안 한 컴퓨터를 시작점으로 DFS 한 번 = 네트워크 1개
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer
