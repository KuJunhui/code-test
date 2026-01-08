from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    MAX = 102
    board = [[0] * MAX for _ in range(MAX)]

    # 1. 모든 직사각형 영역을 1로 채운다 (스케일 2배)
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] = 1

    # 2. 직사각형 내부(테두리 제외) 는 0으로 지운다
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 0

    # 3. BFS로 테두리(값이 1인 곳)만 따라 이동
    sx, sy = characterX * 2, characterY * 2
    ex, ey = itemX * 2, itemY * 2

    # 상, 하, 좌, 우
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited = [[-1] * MAX for _ in range(MAX)]
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 0

    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            return visited[x][y] // 2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < MAX and 0 <= ny < MAX:
                # 테두리(1)이고 아직 방문 안했으면 이동
                if board[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return -1
