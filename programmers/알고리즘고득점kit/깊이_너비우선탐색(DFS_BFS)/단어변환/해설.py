from collections import deque

def solution(begin, target, words):
    # target이 words에 없으면 변환 불가
    if target not in words:
        return 0

    # 두 단어가 한 글자만 다른지 체크하는 함수
    def can_change(a, b):
        diff = 0
        for x, y in zip(a, b):
            if x != y:
                diff += 1
            if diff > 1:
                return False
        return diff == 1

    q = deque()
    q.append((begin, 0))  # (현재 단어, 단계 수)
    visited = set()

    while q:
        word, step = q.popleft()

        if word == target:
            return step

        for w in words:
            if w not in visited and can_change(word, w):
                visited.add(w)
                q.append((w, step + 1))

    return 0  # 변환 불가

# 1 2 3 4 5