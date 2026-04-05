from collections import deque

def solution(n, infection, edges, k):
    # 그래프 저장
    graph = [[] for _ in range(n + 1)]
    for a, b, t in edges:
        graph[a].append((b, t))
        graph[b].append((a, t))

    # 현재 감염 상태 mask에서 type_num 파이프를 열었을 때
    # 최종 감염 상태(mask)를 반환
    def spread(mask, type_num):
        new_mask = mask
        q = deque()

        # 현재 감염된 노드들을 큐에 넣기
        for node in range(1, n + 1):
            if mask & (1 << node):
                q.append(node)

        while q:
            now = q.popleft()
            for nxt, t in graph[now]:
                if t == type_num and not (new_mask & (1 << nxt)):
                    new_mask |= (1 << nxt)
                    q.append(nxt)

        return new_mask

    # 초기 감염 상태
    start_mask = 1 << infection
    states = {start_mask}

    for _ in range(k):
        next_states = set()

        for state in states:
            for pipe_type in (1, 2, 3):
                new_state = spread(state, pipe_type)
                next_states.add(new_state)

        states = next_states

    # 각 상태에서 감염된 노드 수(bit count)의 최댓값 반환
    return max(bin(state).count('1') for state in states)

