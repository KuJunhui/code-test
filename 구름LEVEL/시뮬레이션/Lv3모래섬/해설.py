# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 1) flood_time(dist) 계산: 멀티 소스 BFS (초기 물(0)에서 시작)
dist = [[-1] * M for _ in range(N)]
q = deque()

for y in range(N):
    for x in range(M):
        if grid[y][x] == 0:
            dist[y][x] = 0
            q.append((y, x))

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    y, x = q.popleft()
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and dist[ny][nx] == -1:
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))

# 모래(1) 칸 중 최대 flood_time
Tmax = 0
for y in range(N):
    for x in range(M):
        if grid[y][x] == 1:
            if dist[y][x] > Tmax:
                Tmax = dist[y][x]

# 2) t분 후 섬 개수 >= 2 인지 체크하는 함수
def has_two_islands(t: int) -> bool:
    visited = [[False] * M for _ in range(N)]
    islands = 0

    for y in range(N):
        for x in range(M):
            # t분 후 남아있는 모래: dist > t
            if dist[y][x] > t and not visited[y][x]:
                islands += 1
                if islands >= 2:
                    return True

                dq = deque([(y, x)])
                visited[y][x] = True
                while dq:
                    cy, cx = dq.popleft()
                    for dy, dx in dirs:
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < N and 0 <= nx < M:
                            if dist[ny][nx] > t and not visited[ny][nx]:
                                visited[ny][nx] = True
                                dq.append((ny, nx))

    return False

# 3) t=1..Tmax 순회하며 최초로 섬이 2개 이상이 되는 t 출력
answer = -1
for t in range(1, Tmax + 1):
    if has_two_islands(t):
        answer = t
        break

print(answer)
