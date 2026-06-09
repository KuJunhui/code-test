from collections import defaultdict, deque


def solution(board, commands):
    n = len(board)
    m = len(board[0])

    # 1) 앱 내부 셀 좌표 수집
    cells = defaultdict(list)
    for y in range(n):
        for x in range(m):
            if board[y][x] != 0:
                cells[board[y][x]].append((y, x))

    # 2) 앱 위치/크기 계산
    info = {}
    for app_id, yx in cells.items():
        max_x = max(x for y, x in yx)
        min_x = min(x for y, x in yx)
        min_y = min(y for y, x in yx)

        size = max_x - min_x + 1
        info[app_id] = [min_y, min_x, size]

    # 3) 앱 삭제
    def remove_app(y, x, size):
        for dy in range(y, y + size):
            for dx in range(x, x + size):
                board[dy][dx] = 0

    # 4) 앱 한 칸 밀기
    def push(app_id, direction, reinsert_queue):
        y, x, size = info[app_id]
        # 오른쪽
        if direction == 1:
            if x + size < m:  # 격자 내부 이동
                # 왼쪽 세로줄 삭제
                for dy in range(y, y + size):
                    board[dy][x] = 0
                # 오른쪽 세로줄 추가
                for dy in range(y, y + size):
                    while board[dy][x + size] != 0:
                        push(board[dy][x + size], direction, reinsert_queue)
                    board[dy][x + size] = app_id
                info[app_id][1] = x + 1

            else:  # 앱 삭제 및 반대편 삽입
                remove_app(y, x, size)
                info[app_id][1] = 0
                reinsert_queue.append((app_id, direction))
        # 왼쪽
        elif direction == 3:
            if x > 0:  # 격자 내부 이동
                # 오른쪽 세로줄 삭제
                for dy in range(y, y + size):
                    board[dy][x + size - 1] = 0

                # 왼쪽 세로줄 추가
                for dy in range(y, y + size):
                    while board[dy][x - 1] != 0:
                        push(board[dy][x - 1], direction, reinsert_queue)
                    board[dy][x - 1] = app_id
                info[app_id][1] = x - 1

            else:  # 앱 삭제 및 반대편 삽입
                remove_app(y, x, size)
                info[app_id][1] = m - size
                reinsert_queue.append((app_id, direction))
        # 아래쪽
        elif direction == 2:
            if y + size < n:  # 격자 내부 이동
                # 위 가로줄 삭제
                for dx in range(x, x + size):
                    board[y][dx] = 0

                # 아래 가로줄 추가
                for dx in range(x, x + size):
                    while board[y + size][dx] != 0:
                        push(board[y + size][dx], direction, reinsert_queue)
                    board[y + size][dx] = app_id
                info[app_id][0] = y + 1

            else:  # 앱 삭제 및 반대편 삽입
                remove_app(y, x, size)
                info[app_id][0] = 0
                reinsert_queue.append((app_id, direction))
        # 위쪽
        elif direction == 4:
            if y > 0:  # 격자 내부 이동
                # 아래 가로줄 삭제
                for dx in range(x, x + size):
                    board[y + size - 1][dx] = 0

                # 위 가로줄 추가
                for dx in range(x, x + size):
                    while board[y - 1][dx] != 0:
                        push(board[y - 1][dx], direction, reinsert_queue)
                    board[y - 1][dx] = app_id
                info[app_id][0] = y - 1

            else:  # 앱 삭제 및 반대편 삽입
                remove_app(y, x, size)
                info[app_id][0] = n - size
                reinsert_queue.append((app_id, direction))

    # 5) 앱 반대편에 삽입
    def reinsert(app_id, direction, reinsert_queue):
        y, x, size = info[app_id]
        # 오른쪽
        if direction == 1:
            # 왼쪽부터 세로줄 추가
            for dx in range(size):
                for dy in range(y, y + size):
                    while board[dy][dx] != 0:
                        push(board[dy][dx], direction, reinsert_queue)
                    board[dy][dx] = app_id
        # 왼쪽
        elif direction == 3:
            # 오른쪽부터 세로줄 추가
            for dx in range(m - 1, x - 1, -1):
                for dy in range(y, y + size):
                    while board[dy][dx] != 0:
                        push(board[dy][dx], direction, reinsert_queue)
                    board[dy][dx] = app_id

        # 아래쪽
        elif direction == 2:
            # 위쪽부터 가로줄 추가
            for dy in range(size):
                for dx in range(x, x + size):
                    while board[dy][dx] != 0:
                        push(board[dy][dx], direction, reinsert_queue)
                    board[dy][dx] = app_id

        # 위쪽
        elif direction == 4:
            # 아래쪽부터 가로줄 추가
            for dy in range(n - 1, y - 1, -1):
                for dx in range(x, x + size):
                    while board[dy][dx] != 0:
                        push(board[dy][dx], direction, reinsert_queue)
                    board[dy][dx] = app_id

    # 6) 명령 실행
    for ID, direction in commands:
        reinsert_queue = deque()

        push(ID, direction, reinsert_queue)
        while reinsert_queue:
            r_id, r_direction = reinsert_queue.popleft()
            reinsert(r_id, r_direction, reinsert_queue)

    return board

