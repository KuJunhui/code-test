def solution(dist_limit, split_limit):
    D = dist_limit
    S = split_limit

    pow2 = [1]
    while pow2[-1] <= S:
        pow2.append(pow2[-1] * 2)

    pow3 = [1]
    while pow3[-1] <= S:
        pow3.append(pow3[-1] * 3)

    def need_two(a, m):
        # 2-분기 깊이 a개를 거쳐
        # 3-분기를 달 수 있는 자리 m개를 만들기 위한 최소 분배 노드 수
        total = 0
        x = 2
        for _ in range(a):
            total += (m + x - 1) // x   # ceil(m / x)
            x *= 2
        return total

    answer = 1

    for a in range(len(pow2)):
        if pow2[a] > S:
            break

        # 3-분기 없이 2-분기만 쓰는 경우
        answer = max(answer, 1 + min(D, pow2[a] - 1))

        for b in range(1, len(pow3)):
            if pow2[a] * pow3[b] > S:
                break

            cap3 = (pow3[b] - 1) // 2  # 자리 1개당 3-분기에서 쓸 수 있는 최대 분배 노드 수
            full_need = (pow2[a] - 1) + pow2[a] * cap3  # 완전하게 만들 때 필요한 분배 노드 수

            # 완전하게 만들 수 있으면 정답은 리프 개수 그대로
            if full_need <= D:
                answer = max(answer, pow2[a] * pow3[b])
                continue

            # dist_limit 안에서 만들 수 있는 최대 리프 수 계산
            lo, hi = 1, pow2[a]
            best = pow2[a]

            while lo <= hi:
                mid = (lo + hi) // 2
                if need_two(a, mid) + mid * cap3 >= D:
                    best = mid
                    hi = mid - 1
                else:
                    lo = mid + 1

            prefix = need_two(a, best)

            # prefix만큼 2-분기에 쓰고, 남은 건 전부 3-분기에 쓰는 게 최선
            answer = max(answer, 1 + 2 * D - prefix)

    return answer
