import heapq


def solution(city, road):
    m = len(road)
    INF = float('inf')

    # 1) 도시 좌표를 튜플로 변환
    city_points = [(x, y) for x, y in city]

    # 2) 각 점의 "카메라 제한 속도"
    point_limit = {}

    # 3) 한 점에 카메라가 여러 개면 제한 속도 중 최솟값을 저장
    def set_camera_limit(p, limit):
        if p in point_limit:
            point_limit[p] = min(point_limit[p], limit)
        else:
            point_limit[p] = limit

    # 4) 각 도로 위에서 그래프 분할에 필요한 점들 저장
    road_points = [set() for _ in range(m)]

    # 5) 각 도로의 양 끝점 + 카메라(중점) 추가
    for i, (x1, y1, x2, y2, limit) in enumerate(road):
        road_points[i].add((x1, y1))
        road_points[i].add((x2, y2))
        mid = ((x1 + x2) // 2, (y1 + y2) // 2)
        road_points[i].add(mid)
        set_camera_limit(mid, limit)

    # 6) 점 p가 도로 r 위에 있는지 판정
    def point_on_road(p, r):
        x, y = p
        x1, y1, x2, y2, _ = r
        if y1 == y2:  # horizontal
            return y == y1 and x1 <= x <= x2
        else:  # vertical
            return x == x1 and y1 <= y <= y2

    # 7) 두 도로 r1, r2의 교점을 반환 (만나지 않으면 None)
    # 둘 다 수평/수직이면 끝점 접촉만, 수평×수직이면 실제 교차점 계산
    def intersection_point(r1, r2):
        x1, y1, x2, y2, _ = r1
        a1, b1, a2, b2, _ = r2

        h1 = (y1 == y2)
        h2 = (b1 == b2)

        # 둘 다 수평
        if h1 and h2:
            if y1 != b1:
                return None
            # 같은 y 위에서 한 점만 만나는 경우(끝점 접촉)
            pts1 = {(x1, y1), (x2, y2)}
            pts2 = {(a1, b1), (a2, b2)}
            common = pts1 & pts2
            if common:
                return next(iter(common))
            return None

        # 둘 다 수직
        elif (not h1) and (not h2):
            if x1 != a1:
                return None
            pts1 = {(x1, y1), (x2, y2)}
            pts2 = {(a1, b1), (a2, b2)}
            common = pts1 & pts2
            if common:
                return next(iter(common))
            return None

        # 하나는 수평, 하나는 수직
        elif h1 and not h2:  # 교차
            if x1 <= a1 <= x2 and b1 <= y1 <= b2:
                return (a1, y1)
            return None
        else:
            if a1 <= x1 <= a2 and y1 <= b1 <= y2:
                return (x1, b1)
            return None

    # 8) 도시가 지나가는 도로에 도시 위치 추가
    for p in city_points:
        for ri, r in enumerate(road):
            if point_on_road(p, r):
                road_points[ri].add(p)

    # 9) 도로끼리 만나는 교점 추가
    for i in range(m):
        for j in range(i + 1, m):
            p = intersection_point(road[i], road[j])
            if p is not None:
                road_points[i].add(p)
                road_points[j].add(p)

    # 10) 점 압축(id 부여)
    point_id = {}
    points = []

    def get_id(p):
        if p not in point_id:
            point_id[p] = len(points)
            points.append(p)
        return point_id[p]

    for r_p in road_points:
        for p in r_p:
            get_id(p)

    V = len(points)

    # 11) 그래프 구성
    graph = [[] for _ in range(V)]

    def add_edge(u, v):
        graph[u].append(v)
        graph[v].append(u)

    for i, (x1, y1, x2, y2, _) in enumerate(road):
        pts = list(road_points[i])

        if y1 == y2:  # horizontal
            pts.sort(key=lambda p: p[0])
        else:  # vertical
            pts.sort(key=lambda p: p[1])

        for a, b in zip(pts, pts[1:]):
            u, v = get_id(a), get_id(b)
            add_edge(u, v)

    # 12) 각 정점의 제한값(카메라 없으면 INF)
    node_limit = [INF] * V
    for p in point_limit:
        node_limit[point_id[p]] = point_limit[p]

    # 13) 1번 도시에서 widest path
    # dist[v] = v까지 갈 때 가능한 "최대 일정 속도"
    start = point_id[city_points[0]]
    dist = [-1] * V
    dist[start] = INF
    pq = [(-INF, start)]

    while pq:
        cur_neg, u = heapq.heappop(pq)
        cur = -cur_neg
        if cur < dist[u]:
            continue

        for v in graph[u]:
            cand = min(cur, node_limit[v])
            if cand > dist[v]:
                dist[v] = cand
                heapq.heappush(pq, (-cand, v))

    # 14) 2 ~ n번 도시의 최고 속도를 번호 순으로 구성
    answer = []
    for p in city_points[1:]:
        d = dist[point_id[p]]
        answer.append(0 if d >= INF else d)

    return answer
