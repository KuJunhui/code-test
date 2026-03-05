from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    # 그래프 구성
    for a, b in tickets:
        graph[a].append(b)

    # 사전순으로 가장 앞선 경로를 만들기 위해 역순 정렬
    for a in graph:
        graph[a].sort(reverse=True)

    stack = ["ICN"]
    route = []

    # Hierholzer 알고리즘 (오일러 경로)
    while stack:
        cur = stack[-1]
        if graph[cur]:               # 갈 곳이 남아있으면
            stack.append(graph[cur].pop())  # 사전순으로 가장 앞선 곳으로 이동
        else:                         # 더 갈 곳이 없으면 경로 확정
            route.append(stack.pop())

    return route[::-1]
