from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    visited = [[0] * 102 for _ in range(102)]

    for rec in rectangle:
        x1, y1, x2, y2 = rec[0] * 2, rec[1] * 2, rec[2] * 2, rec[3] * 2
        # 테두리 1로 설정
        # 좌변, 우변 1로 설정
        for y in range(y1, y2 + 1):
            visited[y][x1] = 1
            visited[y][x2] = 1
        # 밑변, 윗변 1로 설정
        for x in range(x1, x2 + 1):
            visited[y1][x] = 1
            visited[y2][x] = 1

    # 내부 2로 설정
    for rec in rectangle:
        x1, y1, x2, y2 = rec[0] * 2 + 1, rec[1] * 2 + 1, rec[2] * 2 - 1, rec[3] * 2 - 1
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                visited[y][x] = 2
    # print([row[0:10] for row in visited[0:10]])
    # 상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    q = deque()
    q.append((characterX * 2, characterY * 2, 0))
    visited[characterY * 2][characterX * 2] = 2

    while q:
        character_x, character_y, distance = q.popleft()
        # print("x y", character_x, character_y)
        # print("distance", distance)
        if character_x == itemX * 2 and character_y == itemY * 2:
            return distance / 2

        for i in range(4):
            nx = character_x + dx[i]
            ny = character_y + dy[i]

            if 0 < nx < 101 and 0 < ny < 101:
                if visited[ny][nx] == 1:
                    visited[ny][nx] = 2
                    q.append((nx, ny, distance + 1))
                    # print("nx ny", nx, ny)

    return 0

# 입출력 예 #3
# rectangle	    characterX	characterY	 itemX	 itemY	 result
# [[1,1,5,7]]	    1	         1	        4	   7	    9

# 1 2 3