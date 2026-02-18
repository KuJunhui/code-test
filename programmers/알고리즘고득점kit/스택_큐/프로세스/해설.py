from collections import deque

def solution(priorities, location):
    q = deque((p, i) for i, p in enumerate(priorities))  # (우선순위, 원래 인덱스)
    order = 0

    while q:
        p, i = q.popleft()

        # 큐 안에 더 높은 우선순위가 있으면 뒤로 보냄
        if any(p2 > p for p2, _ in q):
            q.append((p, i))
        else:
            # 실행(종료)
            order += 1
            if i == location:
                return order
