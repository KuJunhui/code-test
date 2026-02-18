def solution(arrows):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    x, y = 0, 0

    visited_nodes = {(x, y)}
    visited_edges = set()  # undirected edge: ((x1,y1),(x2,y2)) normalized
    rooms = 0

    for d in arrows:
        # 교차점 처리를 위해 1칸 이동을 2번으로 쪼갬
        for _ in range(2):
            nx, ny = x + dx[d], y + dy[d]

            a = (x, y)
            b = (nx, ny)
            edge = (a, b) if a <= b else (b, a)

            # "처음 보는 간선"으로 "이미 방문한 정점"에 들어가면 사이클 1개 생성
            if edge not in visited_edges:
                if b in visited_nodes:
                    rooms += 1
                visited_edges.add(edge)

            visited_nodes.add(b)
            x, y = nx, ny

    return rooms
