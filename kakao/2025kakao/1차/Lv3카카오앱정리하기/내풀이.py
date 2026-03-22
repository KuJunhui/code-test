from collections import deque, defaultdict

def solution(board, commands):
    N = len(board)
    M = len(board[0])

    # 앱 정보: info[id] = [top, left, size]
    cells = defaultdict(list)
    for i in range(N):
        for j in range(M):
            app_id = board[i][j]
            if app_id == 0:
                continue
            cells[app_id].append((i, j))

    info = {}
    for app_id, pos_list in cells.items():
        min_r = min(r for r, c in pos_list)
        max_r = max(r for r, c in pos_list)
        min_c = min(c for r, c in pos_list)

        size = max_r - min_r + 1
        info[app_id] = [min_r, min_c, size]

    def remove_square(app_id, r, c, size):
        for i in range(r, r + size):
            for j in range(c, c + size):
                if board[i][j] == app_id:
                    board[i][j] = 0

    def push(app_id, direction, wrap_queue):
        r, c, size = info[app_id]

        # 1: 오른쪽
        if direction == 1:
            if c < M - size:
                # 왼쪽 한 줄 제거
                for i in range(r, r + size):
                    board[i][c] = 0

                # 오른쪽 새 한 줄 채우기
                new_col = c + size
                for i in range(r, r + size):
                    while board[i][new_col] != 0:
                        push(board[i][new_col], direction, wrap_queue)
                    board[i][new_col] = app_id

                info[app_id][1] = c + 1
            else:
                # wrap: 일단 완전히 제거하고, 나중에 반대편 삽입
                remove_square(app_id, r, c, size)
                info[app_id][1] = 0
                wrap_queue.append((app_id, direction))

        # 3: 왼쪽
        elif direction == 3:
            if c > 0:
                # 오른쪽 한 줄 제거
                for i in range(r, r + size):
                    board[i][c + size - 1] = 0

                # 왼쪽 새 한 줄 채우기
                new_col = c - 1
                for i in range(r, r + size):
                    while board[i][new_col] != 0:
                        push(board[i][new_col], direction, wrap_queue)
                    board[i][new_col] = app_id

                info[app_id][1] = c - 1
            else:
                remove_square(app_id, r, c, size)
                info[app_id][1] = M - size
                wrap_queue.append((app_id, direction))

        # 2: 아래
        elif direction == 2:
            if r < N - size:
                # 위쪽 한 줄 제거
                for j in range(c, c + size):
                    board[r][j] = 0

                # 아래쪽 새 한 줄 채우기
                new_row = r + size
                for j in range(c, c + size):
                    while board[new_row][j] != 0:
                        push(board[new_row][j], direction, wrap_queue)
                    board[new_row][j] = app_id

                info[app_id][0] = r + 1
            else:
                remove_square(app_id, r, c, size)
                info[app_id][0] = 0
                wrap_queue.append((app_id, direction))

        # 4: 위
        else:
            if r > 0:
                # 아래쪽 한 줄 제거
                for j in range(c, c + size):
                    board[r + size - 1][j] = 0

                # 위쪽 새 한 줄 채우기
                new_row = r - 1
                for j in range(c, c + size):
                    while board[new_row][j] != 0:
                        push(board[new_row][j], direction, wrap_queue)
                    board[new_row][j] = app_id

                info[app_id][0] = r - 1
            else:
                remove_square(app_id, r, c, size)
                info[app_id][0] = N - size
                wrap_queue.append((app_id, direction))

    def insert_wrapped(app_id, direction, wrap_queue):
        r, c, size = info[app_id]

        # 오른쪽으로 밀려서 왼쪽에 등장
        if direction == 1:
            for j in range(0, size):
                for i in range(r, r + size):
                    while board[i][j] != 0:
                        push(board[i][j], direction, wrap_queue)
                    board[i][j] = app_id

        # 왼쪽으로 밀려서 오른쪽에 등장
        elif direction == 3:
            for j in range(M - 1, M - size - 1, -1):
                for i in range(r, r + size):
                    while board[i][j] != 0:
                        push(board[i][j], direction, wrap_queue)
                    board[i][j] = app_id

        # 아래로 밀려서 위쪽에 등장
        elif direction == 2:
            for i in range(0, size):
                for j in range(c, c + size):
                    while board[i][j] != 0:
                        push(board[i][j], direction, wrap_queue)
                    board[i][j] = app_id

        # 위로 밀려서 아래쪽에 등장
        else:
            for i in range(N - 1, N - size - 1, -1):
                for j in range(c, c + size):
                    while board[i][j] != 0:
                        push(board[i][j], direction, wrap_queue)
                    board[i][j] = app_id

    for app_id, direction in commands:
        wrap_queue = deque()

        # 현재 명령의 원래 push 수행
        push(app_id, direction, wrap_queue)

        # 격자 밖으로 나간 앱들을 차례대로 반대편에 다시 삽입
        while wrap_queue:
            wrapped_id, wrapped_dir = wrap_queue.popleft()
            insert_wrapped(wrapped_id, wrapped_dir, wrap_queue)

    return board

# 1 