from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    for a, b in tickets:
        graph[a].append(b)

    for a in graph:
        graph[a].sort(reverse=True)

    stack = ['ICN']
    result = []

    # 오일러 경로
    while stack:
        cur = stack[-1]
        if graph[cur]:
            stack.append(graph[cur].pop())
        else:
            result.append(stack.pop())

    return result[::-1]
