def solution(dist_limit, split_limit):
    D, S = dist_limit, split_limit
    answer = 1

    # cost(a, m) = 2-분기 깊이 a개를 지나
    # 3-분기 시작점에 m개의 노드를 만들기 위한 최소 분배 노드 수
    def cost(a, m):
        total = 0
        p = 2
        for _ in range(a):
            total += (m + p - 1) // p
            p <<= 1
        return total

    p2 = 1  # 2^a
    a = 0
    while p2 <= S:
        # 3-분기 구간이 없는 경우
        answer = max(answer, 1 + min(D, p2 - 1))

        p3 = 3
        while p2 * p3 <= S:
            cap = (p3 - 1) // 2   # 시작 노드 1개당 3-분기에서 쓸 수 있는 최대 분배 노드 수

            # m개 시작 노드를 만들었을 때 필요한 총 분배 노드 수
            def need(m):
                return cost(a, m) + m * cap

            # m = p2(최대)까지 써도 dist_limit를 못 채우면 완전하게 만드는 게 최선
            if need(p2) <= D:
                answer = max(answer, p2 * p3)
            else:
                # dist_limit를 넘기지 않으면서 최대한 많은 리프를 만드는 최소 m 탐색
                lo, hi = 1, p2
                while lo < hi:
                    mid = (lo + hi) // 2
                    if need(mid) >= D:
                        hi = mid
                    else:
                        lo = mid + 1

                prefix = cost(a, lo)
                # 남은 분배 노드는 전부 3-분기에 쓰는 것이 최선
                answer = max(answer, 1 + 2 * D - prefix)

            p3 *= 3

        p2 <<= 1
        a += 1

    return answer