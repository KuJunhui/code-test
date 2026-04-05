def solution(arr):
    numbers = list(map(int, arr[::2]))
    ops = arr[1::2]
    n = len(numbers)
    # dp_max[i][j] : i~j 구간 식의 최댓값
    # dp_min[i][j] : i~j 구간 식의 최솟값
    dp_max = [[-float('inf')] * n for _ in range(n)]
    dp_min = [[float('inf')] * n for _ in range(n)]

    # 길이 1 구간 초기화
    for i in range(n):
        dp_max[i][i] = numbers[i]
        dp_min[i][i] = numbers[i]

    # 구간 길이 2 이상
    for length in range(2, n + 1):  # 구간 길이
        for i in range(n - length + 1):
            j = i + length - 1
            # i~j 구간을 k 기준으로 분할
            for k in range(i, j):
                op = ops[k]

                if op == '+':
                    max_val = dp_max[i][k] + dp_max[k + 1][j]
                    min_val = dp_min[i][k] + dp_min[k + 1][j]
                else:  # op == '-'
                    max_val = dp_max[i][k] - dp_min[k + 1][j]
                    min_val = dp_min[i][k] - dp_max[k + 1][j]

                dp_max[i][j] = max(dp_max[i][j], max_val)
                dp_min[i][j] = min(dp_min[i][j], min_val)

    return dp_max[0][n - 1]
