def solution(triangle):
    # dp를 triangle과 같은 모양으로 복사해서 사용
    dp = [row[:] for row in triangle]
    n = len(triangle)

    # 1번째 줄부터 마지막 줄까지 채우기
    for i in range(1, n):
        for j in range(i + 1):  # i번째 줄은 0 ~ i까지 인덱스
            if j == 0:
                # 맨 왼쪽
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == i:
                # 맨 오른쪽
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                # 중간 값들
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    # 마지막 줄에서 최댓값이 정답
    return max(dp[-1])

# 1 2 3 4 5