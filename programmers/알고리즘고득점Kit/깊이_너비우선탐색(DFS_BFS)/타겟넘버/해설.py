from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers)

    # bfs
    q = deque()
    q.append((0, 0))

    while q:
        i, total = q.popleft()
        if i == n and target == total:
            answer += 1

        if i < n:
            q.append((i + 1, total + numbers[i]))
            q.append((i + 1, total - numbers[i]))

    return answer