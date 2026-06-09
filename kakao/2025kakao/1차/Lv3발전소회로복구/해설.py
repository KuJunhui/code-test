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

    # 2) 패널들의 좌표 수집
    points = []
    for h, y, x in panels:
        points.append((h - 1, y - 1, x - 1))

    # 3) 각 패널에서 BFS, 벽 제외한 칸들의 최단거리표 리턴
    def bfs(sy, sx):
        dist = [[-1] * m for _ in range(n)]
        q = deque([(sy, sx)])
        dist[sy][sx] = 0

        while q:
            y, x = q.popleft()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ny = y + dy
                nx = x + dx
                if 0 <= ny < n and 0 <= nx < m and dist[ny][nx] == -1 and grid[ny][nx] != '#':
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
        return dist

    # 4) 각 패널이 출발점인 최단거리표 구성
    all_bfs = []
    for h, y, x in points:
        all_bfs.append(bfs(y, x))

    # 5) 패널간 최단거리 구성
    dist2d = [[INF] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            h, ty, tx = points[j]
            dist2d[i][j] = all_bfs[i][ty][tx]

    # 6) 각 패널에서 엘리베이터까지 최단거리 구성
    to_elev = [all_bfs[i][ey][ex] for i in range(k)]

    # 7) 패널간 3D 이동시간 계산
    def move_time(a, b):
        h1, y1, x1 = points[a]
        h2, y2, x2 = points[b]

        if h1 == h2:
            return dist2d[a][b]
        return to_elev[a] + abs(h1 - h2) + to_elev[b]

    # 8) 1번 패널에서 각 패널까지 3D 이동시간 구성
    start_idx = 0
    start_cost = [0] * k
    for i in range(k):
        start_cost[i] = move_time(start_idx, i)

    # 9) 선행 조건 비트마스크화
    prereq = [0] * k
    for a, b in seqs:
        prereq[b - 1] |= (1 << (a - 1))

    # 10) 비트마스크 DP 초기 상태
    # dp[mask][i] = mask 패널들을 활성화했고 마지막 활성화 패널이 i일 때 최소이동시간
    size = 1 << k
    dp = [[INF] * k for _ in range(size)]
    for i in range(k):
        if prereq[i] == 0:
            mask = 1 << i
            dp[mask][i] = start_cost[i]

    # 11) 상태 전이
    for mask in range(size):
        for i in range(k):
            # 도달한 적 없는 상태는 무시
            if dp[mask][i] == INF:
                continue

            for j in range(k):
                # 이미 활성화한 패널인지 확인
                if mask & (1 << j):
                    continue
                # 선행 조건 확인
                if (prereq[j] & mask) != prereq[j]:
                    continue
                # 다음 패널 활성화 및 최소이동시간 갱신
                nxt = mask | (1 << j)
                time = dp[mask][i] + move_time(i, j)
                if time < dp[nxt][j]:
                    dp[nxt][j] = time

    return min(dp[size - 1])

