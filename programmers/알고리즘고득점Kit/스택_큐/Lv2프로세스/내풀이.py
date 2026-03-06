from collections import deque

def solution(priorities, location):
    max_p = max(priorities)
    q = deque()
    for idx, p in enumerate(priorities):
        q.append((idx, p))

    seq = 1
    while q:
        idx, p = q.popleft()
        if p >= max_p:
            if idx == location:
                return seq
            priorities[idx] = 0
            max_p = max(priorities)
            seq += 1
            continue
        else:
            q.append((idx, p))
