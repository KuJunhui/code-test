from collections import deque

def solution(board):
    rows = len(board)
    cols = len(board[0])

    # R(시작), G(목표) 위치 찾기
    start = goal = None
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'R':
                start = (r, c)
            elif board[r][c] == 'G':
                goal = (r, c)

    # 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = {start}
    queue = deque([(start[0], start[1], 0)])

    while queue:
        r, c, dist = queue.popleft()

        if (r, c) == goal:
            return dist

        for dr, dc in directions:
            nr, nc = r, c
            # 장애물이나 벽에 부딪힐 때까지 미끄러짐
            while True:
                tr, tc = nr + dr, nc + dc
                if tr < 0 or tr >= rows or tc < 0 or tc >= cols:
                    break
                if board[tr][tc] == 'D':
                    break
                nr, nc = tr, tc

            if (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1
