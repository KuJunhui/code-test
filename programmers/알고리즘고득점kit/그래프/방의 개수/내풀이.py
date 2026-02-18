def solution(arrows):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]
    x, y = 0, 0

    visited_nodes = set()
    visited_edges = set()
    visited_nodes.add((x, y))
    room_cnt = 0
    for arrow in arrows:
        for _ in range(2):
            nx = x + dx[arrow]
            ny = y + dy[arrow]
            a = (x, y)
            b = (nx, ny)

            edge = (a, b) if a <= b else (b, a)
            if edge not in visited_edges:
                if b in visited_nodes:
                    room_cnt += 1
                visited_edges.add(edge)
            visited_nodes.add(b)
            x, y = nx, ny

    return room_cnt
