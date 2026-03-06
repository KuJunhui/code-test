def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    # 교집합 (도난 당했지만 자기 여벌로 해결한 학생)
    overlap = lost_set & reserve_set
    lost = sorted(list(lost_set - overlap))
    reserve = sorted(list(reserve_set - overlap))

    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)

    return n - len(lost)
