T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    grid = [[] * m for _ in range(n)]

    for y in range(n):
        row = input()
        for x in range(m):
            grid[y].append(row[x])

    def check_row():
        cnt = 0
        for y in range(n):
            temp = 0
            for x in range(m):
                if grid[y][x] == '#':
                    temp += 1
            if temp == m:
                cnt += 1
        return cnt

    def check_col():
        cnt = 0
        for x in range(m):
            temp = 0
            for y in range(n):
                if grid[y][x] == '#':
                    temp += 1
            if temp == n:
                cnt += 1
        return cnt

    if n >= m:
        col = check_col()
        if col == m:
            print(col)
        else:
            row = check_row()
            print(col + row)
    else:
        row = check_row()
        if row == n:
            print(row)
        else:
            col = check_col()
            print(col + row)