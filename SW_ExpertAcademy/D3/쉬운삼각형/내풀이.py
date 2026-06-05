from collections import defaultdict

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    x_y_list = []
    for _ in range(N):
        x, y = map(int, input().split())
        x_y_list.append((x, y))

    x_graph = defaultdict(list)
    y_graph = defaultdict(list)
    for x, y in x_y_list:
        x_graph[x].append(y)
        y_graph[y].append(x)

    maximum = 0
    for x, y in x_y_list:  # 각 점을 직각의 꼭짓점이라고 가정
        # 같은 y좌표를 가진 점들 중 x 차이 최댓값
        xl = y_graph[y]
        if len(xl) < 2:
            continue
        max_dx = max(abs(x - other_x) for other_x in xl)

        # 같은 x좌표를 가진 점들 중 y 차이 최댓값
        yl = x_graph[x]
        if len(yl) < 2:
            continue
        max_dy = max(abs(y - other_y) for other_y in yl)

        if maximum < max_dx * max_dy:
            maximum = max_dx * max_dy

    print(maximum)
