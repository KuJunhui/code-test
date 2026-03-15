def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    left, right = 1, distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # 만들고 싶은 최소 거리

        removed = 0
        prev = 0  # 출발지점

        for rock in rocks:
            if rock - prev < mid:
                removed += 1  # 이 바위 제거
            else:
                prev = rock  # 이 바위는 남김

        if removed <= n:
            answer = mid  # mid는 가능
            left = mid + 1  # 더 큰 최소 거리도 시도
        else:
            right = mid - 1  # mid는 불가능

    return answer
