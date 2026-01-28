def solution(m, n, board):
    board = [list(row) for row in board]

    def check_r_b(yx, b):
        check_set = set()
        if board[yx[0]][yx[1] + 1] == b and board[yx[0] + 1][yx[1] + 1] == b and board[yx[0] + 1][yx[1]] == b:
            check_set.add((yx[0], yx[1]))
            check_set.add((yx[0], yx[1] + 1))
            check_set.add((yx[0] + 1, yx[1] + 1))
            check_set.add((yx[0] + 1, yx[1]))
        return check_set

    def delete_b(yx_list, board):
        for yx in yx_list:
            if yx[0] == 0:
                board[yx[0]][yx[1]] = 0
            else:
                for y in range(yx[0], 0, -1):
                    board[y][yx[1]] = board[y - 1][yx[1]]
                board[0][yx[1]] = 0
        return board

    delete_sum = 0
    while 1:
        temp_set = set()

        for y in range(m - 1):
            for x in range(n - 1):
                if board[y][x] != 0:
                    if check_r_b((y, x), board[y][x]):
                        for s in check_r_b((y, x), board[y][x]):
                            temp_set.add(s)

        if not temp_set:
            return delete_sum
        else:
            delete_sum += len(temp_set)
            temp_list = list(temp_set)
            temp_list.sort(key=lambda x: (x[0], x[1]))
            board = delete_b(temp_list, board)
