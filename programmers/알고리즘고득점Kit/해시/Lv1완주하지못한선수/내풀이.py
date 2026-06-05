from collections import Counter


def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)

    p -= c

    return list(p.keys())[0]

