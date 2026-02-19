from collections import deque

def solution(game_board, table):
    n = len(table)
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def bfs_collect(grid, start_i, start_j, target):
        cells = []
        q = deque()
        q.append((start_i, start_j))
        cells.append((start_i, start_j))
        grid[start_i][start_j] = -1
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and grid[ny][nx] == target:
                    q.append((ny, nx))
                    cells.append((ny, nx))
                    grid[ny][nx] = -1
        return cells

    def normalize(cells):
        min_y = min(y for y, x in cells)
        min_x = min(x for y, x in cells)
        cells = sorted((y - min_y, x - min_x) for y, x in cells)
        return cells

    def rotate_90(cells):
        cells = [(-x, y) for y, x in cells]
        return cells

    holes = []
    gb = [row[:] for row in game_board]
    for i in range(n):
        for j in range(n):
            if gb[i][j] == 0:
                cells = bfs_collect(gb, i, j, 0)
                holes.append(normalize(cells))

    blocks = []
    tb = [row[:] for row in table]
    for i in range(n):
        for j in range(n):
            if tb[i][j] == 1:
                cells = bfs_collect(tb, i, j, 1)
                blocks.append(normalize(cells))

    total_count = 0
    used_blocks = [False] * len(blocks)
    for hole in holes:
        for idx, block in enumerate(blocks):
            rotated_block = []
            if used_blocks[idx]:
                continue
            if len(hole) != len(block):
                continue
            else:
                for i in range(4):
                    block = rotate_90(block)
                    rotated_block.append(normalize(block))
                if hole in rotated_block:
                    total_count += len(hole)
                    used_blocks[idx] = True
                    break

    return total_count
