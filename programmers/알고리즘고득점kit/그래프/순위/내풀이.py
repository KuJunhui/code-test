def solution(n, results):
    win = [[False] * (n + 1) for _ in range(n + 1)]

    for x, y in results:
        win[x][y] = True

    # 플로이드-워셜 전파
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if not win[i][k]:
                continue
            for j in range(1, n + 1):
                if win[k][j]:
                    win[i][j] = True

    # 선수 순위 확정 여부
    answer = 0
    for i in range(1, n + 1):
        game = 0
        for j in range(1, n + 1):
            if i == j:
                continue
            if win[i][j] or win[j][i]:
                game += 1
        if game == n - 1:
            answer += 1

    return answer