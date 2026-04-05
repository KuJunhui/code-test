def solution(n, q, w, e, r):
    # q: a승 b패
    # w: a패 b승
    # e: a승 b승
    # r: a패 b패
    prev_win = e
    prev_lose = w
    for i in range(n):
        cur_win = max(prev_win + e, prev_lose + q)
        cur_lose = max(prev_win + w, prev_lose + r)
        prev_win, prev_lose = cur_win, cur_lose

    return max(prev_win, prev_lose)