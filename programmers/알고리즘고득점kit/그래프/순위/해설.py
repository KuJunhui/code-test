def solution(n, results):
    # win[i][j] = i 선수가 j 선수를 이긴 여부 (1-indexed 사용 위해 n+1)
    win = [[False] * (n + 1) for _ in range(n + 1)]

    # 직접 경기 결과 입력
    for a, b in results:
        win[a][b] = True

    # 플로이드-워셜: 이긴 관계 전파
    for k in range(1, n + 1):          # 중간 선수 k
        for i in range(1, n + 1):      # 출발 선수 i
            if not win[i][k]:
                continue
            for j in range(1, n + 1):  # 도착 선수 j
                if win[k][j]:
                    win[i][j] = True

    answer = 0
    # 각 선수의 순위가 정확히 정해지는지 확인
    for i in range(1, n + 1):
        known = 0
        for j in range(1, n + 1):
            if i == j:
                continue
            # i가 j를 이기거나, j가 i를 이기거나 둘 중 하나만 알면 됨
            if win[i][j] or win[j][i]:
                known += 1

        # 각 선수 i에 대해 알고 있는 상대 수가 (n-1) 이면 그 선수의 순위는 확정
        if known == n - 1:
            answer += 1

    return answer

# 1 2 3 4 5