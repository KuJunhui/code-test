def solution(n, q, w, e, r):
    # n = 게임 횟수
    # q = (a 승, b 패)
    # w = (a 패, b 승)
    # e = (a 승, b 승)
    # r = (a 패, b 패)

    if n == 1:
        # 첫 게임은 b가 무조건 승
        return max(w, e)

    # prev_lose = 현재까지 왔을 때 마지막 a가 패인 경우 최대 점수
    # prev_win  = 현재까지 왔을 때 마지막 a가 승인 경우 최대 점수
    prev_lose = w   # 1번째 게임에서 a 패, b 승
    prev_win = e    # 1번째 게임에서 a 승, b 승

    for _ in range(2, n + 1):
        curr_lose = max(
            prev_lose + r,   # 이전 a=패 -> 현재 b=패, 현재 a=패
            prev_win + w     # 이전 a=승 -> 현재 b=승, 현재 a=패
        )
        curr_win = max(
            prev_lose + q,   # 이전 a=패 -> 현재 b=패, 현재 a=승
            prev_win + e     # 이전 a=승 -> 현재 b=승, 현재 a=승
        )

        prev_lose, prev_win = curr_lose, curr_win

    return max(prev_lose, prev_win)