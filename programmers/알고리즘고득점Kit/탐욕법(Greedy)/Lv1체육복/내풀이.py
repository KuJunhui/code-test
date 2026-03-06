def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)

    both = lost & reserve
    lost -= both
    reserve -= both

    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)

    return n - len(lost)
