from collections import deque

def solution(maps):
    len_y = len(maps)
    len_x = len(maps[0])

    # 상대 팀 진영 도착 불가
    if maps[len_y - 1][len_x - 2] == 0 and maps[len_y - 2][len_x - 1] == 0:
        return -1

    # 상,하,좌,우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # BFS
    q = deque()
    q.append((0, 0, 1))
    maps[0][0] = 0

    while q:
        x, y, distance = q.popleft()

        if x == len_x - 1 and y == len_y - 1:
            return distance

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < len_x and 0 <= ny < len_y:
                if maps[ny][nx] == 1:
                    maps[ny][nx] = 0
                    q.append((nx, ny, distance + 1))

    return -1