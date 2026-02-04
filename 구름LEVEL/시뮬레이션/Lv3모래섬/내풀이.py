from collections import deque

n, m = map(int, input().split())

map_info = [list(map(int, input().split())) for _ in range(n)]

tmap_info = [[-1] * m for _ in range(n)]

q = deque()
for y in range(n):
    for x in range(m):
        if map_info[y][x] == 0:
            tmap_info[y][x] = 0
            q.append((y, x))

dy = [-1, 1, 0, 0]
dx = [0 ,0, -1, 1]
t_max = 0

while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and tmap_info[ny][nx] == -1:
            tmap_info[ny][nx] = tmap_info[y][x] + 1
            q.append((ny, nx))
            if t_max < tmap_info[ny][nx]:
                t_max = tmap_info[ny][nx]

def check_two_island(t: int) -> bool:
    island_num = 0
    visited = [[False] * m for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if tmap_info[y][x] > t and not visited[y][x]:
                island_num += 1
                if island_num >= 2:
                    return True
                dy = [-1, 1, 0, 0]
                dx = [0, 0, -1, 1]
                q = deque()
                q.append((y, x))
                while q:
                    y, x = q.popleft()
                    visited[y][x] = True
                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]
                        if 0 <= ny < n and 0 <= nx < m and tmap_info[ny][nx] > t and not visited[ny][nx]:
                            visited[ny][nx] = True
                            q.append((ny, nx))
    return False

for i in range(1, t_max + 1):
    if check_two_island(i):
        print(i)
        exit()
print('-1')

# 1 2 3 4 5