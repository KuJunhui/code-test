def solution(triangle):
    dp = [row[:] for row in triangle]
    n = len(triangle)

    for i in range(1, n):
        for j in range(i + 1):
            # 맨처음
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            # 맨끝
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            # 중간
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    answer = max(dp[-1])

    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))