def solution(n, q, w, e, r):
    # q: (a승, b패)
    # w: (a패, b승)
    # e: (a승, b승)
    # r: (a패, b패)
    if n == 1:
        return max(w, e)

    prev_lose = w
    prev_win = e
    for i in range(2, n + 1):
        cur_lose = max(prev_lose + r, prev_win + w)
        cur_win = max(prev_lose + q, prev_win + e)
        prev_lose, prev_win = cur_lose, cur_win

    return max(prev_lose, prev_win)