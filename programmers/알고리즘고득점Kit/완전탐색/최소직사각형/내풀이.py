def solution(sizes):
    long = []
    short = []
    for w, h in sizes:
        long.append(max(w, h))
        short.append(min(w, h))
    # print(max(long)*max(short))

    return max(long) * max(short)