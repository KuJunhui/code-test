from collections import deque

def solution(n, infection, edges, k):
    # 그래프 저장
    graph = [[] for _ in range(n + 1)]
    for a, b, t in edges:
        graph[a].append((b, t))
        graph[b].append((a, t))

    # 현재 감염 집합(infected)에서 type_num 파이프를 열었을 때
    # 최종 감염 집합을 반환
    def spread(infected, type_num):
        infected = set(infected)
        q = deque(infected)

        while q:
            now = q.popleft()
            for nxt, t in graph[now]:
                if t == type_num and nxt not in infected:
                    infected.add(nxt)
                    q.append(nxt)

        return frozenset(infected)

    # states = 현재까지 가능한 감염 상태들
    states = {frozenset([infection])}
    answer = 1

    for _ in range(k):
        next_states = set()

        for state in states:
            answer = max(answer, len(state))

            for pipe_type in [1, 2, 3]:
                new_state = spread(state, pipe_type)
                next_states.add(new_state)

        states = next_states

    # 마지막 states도 확인
    for state in states:
        answer = max(answer, len(state))

    return answer