def solution(s):
    total = 0
    for idx, a in enumerate(s):
        if total < 0:
            return False
        if a == '(':
            total += 1
        else:
            total -= 1

    if total == 0:
        return True
    return False
