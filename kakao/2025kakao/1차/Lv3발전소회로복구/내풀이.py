from collections import deque

def solution(h, grid, panels, seqs):
    n = len(grid)
    m = len(grid[0])
    k = len(panels)
    INF = float('inf')

    # 1) 엘리베이터 위치 찾기
    ey = ex = -1
    for y in range(n):
        for x in range(m):
            if grid[y][x] == '@':
                ey, ex = y, x
                break

    # 2) 특수 지점(패널들 + 엘리베이터)의 2D 좌표 준비
    #    패널은 0 ~ k-1, 엘리베이터는 k
    points_2d = []
    for h, y, x in panels:
        points_2d.append((h - 1, y - 1, x - 1))

    # 3) 각 특수 지점에서 BFS -> 다른 특수 지점까지의 2D 최단거리
    def bfs(sy, sx):
        dist = [[-1] * m for _ in range(n)]
        q = deque([(sy, sx)])
        dist[sy][sx] = 0

        while q:
            y, x = q.popleft()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m and dist[ny][nx] == -1 and grid[ny][nx] != '#':
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
        return dist

    all_bfs = []
    for h, y, x in points_2d:
        all_bfs.append(bfs(y, x))

    dist2d = [[INF] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            h, ty, tx = points_2d[j]
            if all_bfs[i][ty][tx] != -1:
                dist2d[i][j] = all_bfs[i][ty][tx]

    # 패널 -> 엘리베이터 2D 거리
    to_elev = [all_bfs[i][ey][ex] for i in range(k)]

    # 4) 실제 3D 이동 거리 계산 함수
    def move_cost(a, b):
        h1, x1, y1 = points_2d[a]
        h2, x2, y2 = points_2d[b]

        if h1 == h2:
            return dist2d[a][b]
        return to_elev[a] + abs(h1 - h2) + to_elev[b]

    # 시작 위치는 1번 패널 위치, 시작 위치 -> 각 패널로 이동하는 비용
    start_idx = 0
    start_cost = [0] * k
    for i in range(k):
        start_cost[i] = move_cost(start_idx, i)

    # 5) 선행 조건 비트마스크화
    prereq = [0] * k
    for a, b in seqs:
        prereq[b - 1] |= (1 << (a - 1))

    # 6) 비트마스크 DP
    # dp[mask][i] = mask를 활성화했고 마지막 활성화 패널이 i일 때 최소 시간
    size = 1 << k
    dp = [[INF] * k for _ in range(size)]
    # 초기 상태
    for j in range(k):
        if prereq[j] == 0:
            mask = 1 << j
            dp[mask][j] = start_cost[j]

    # 상태 전이
    for mask in range(size):
        for i in range(k):
            if dp[mask][i] == INF:     # 도달한 적 없는 상태는 무시
                continue

            for j in range(k):
                if mask & (1 << j):     # 이미 활성화한 패널인지 확인
                    continue
                if (prereq[j] & mask) != prereq[j]:     # 선행 조건 확인
                    continue

                nxt = mask | (1 << j)
                cost = dp[mask][i] + move_cost(i, j)
                if cost < dp[nxt][j]:
                    dp[nxt][j] = cost

    return min(dp[size - 1])

# 