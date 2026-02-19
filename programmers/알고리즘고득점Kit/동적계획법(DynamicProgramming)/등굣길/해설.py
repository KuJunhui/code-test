def solution(m, n, puddles):
    MOD = 1_000_000_007

    # dp[y][x] : (1,1)에서 (x,y)까지 가는 경로의 개수
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 물에 잠긴 지역을 set으로 관리 (x, y) = (열, 행)
    puddle_set = {(x, y) for x, y in puddles}

    dp[1][1] = 1  # 시작점

    for y in range(1, n + 1):  # 행 (위에서 아래로)
        for x in range(1, m + 1):  # 열 (왼쪽에서 오른쪽으로)
            if (x, y) in puddle_set:
                dp[y][x] = 0  # 물에 잠긴 곳은 경로 없음
                continue
            if x == 1 and y == 1:
                continue  # 시작점은 이미 1로 세팅됨

            dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % MOD

    return dp[n][m]
