from collections import deque

def solution(game_board, table):
    n = len(game_board)
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    def bfs_collect(grid, start_i, start_j, target):
        """grid에서 target(0 또는 1)인 연결 컴포넌트 좌표들을 수집"""
        q = deque([(start_i, start_j)])
        grid[start_i][start_j] = -1  # 방문 표시
        cells = [(start_i, start_j)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == target:
                    grid[nx][ny] = -1
                    q.append((nx, ny))
                    cells.append((nx, ny))
        return cells

    def normalize(cells):
        """좌표 리스트를 (0,0) 기준으로 이동 + 정렬 + 튜플화"""
        min_x = min(x for x, _ in cells)
        min_y = min(y for _, y in cells)
        norm = sorted((x - min_x, y - min_y) for x, y in cells)
        return tuple(norm)

    def rotate_90(shape):
        """shape: ((x,y), ...) 를 90도 회전한 shape 반환 (정규화는 별도)"""
        # (x,y) -> (y, -x)
        rotated = [(y, -x) for x, y in shape]
        return rotated

    # 1) game_board에서 구멍(0 덩어리) 추출
    gb = [row[:] for row in game_board]
    holes = []
    for i in range(n):
        for j in range(n):
            if gb[i][j] == 0:
                cells = bfs_collect(gb, i, j, 0)
                holes.append(normalize(cells))

    # 2) table에서 블록(1 덩어리) 추출
    tb = [row[:] for row in table]
    blocks = []
    for i in range(n):
        for j in range(n):
            if tb[i][j] == 1:
                cells = bfs_collect(tb, i, j, 1)
                blocks.append(normalize(cells))

    # 3) 구멍 사용 여부 관리
    used = [False] * len(holes)

    # 4) 각 블록을 회전해가며 매칭
    filled = 0
    for block in blocks:
        # block의 4회전 형태 만들기 (정규화된 튜플들)
        rotations = []
        cur = list(block)
        for _ in range(4):
            cur = rotate_90(cur)
            rotations.append(normalize(cur))

        # 아직 안 쓴 hole 중 하나와 매칭 시도
        for hi, hole in enumerate(holes):
            if used[hi]:
                continue
            # 크기 다르면 바로 패스
            if len(hole) != len(block):
                continue
            # 회전 중 하나라도 같으면 매칭 성공
            if hole in rotations:
                used[hi] = True
                filled += len(hole)
                break

    return filled
