def solution(n, times):
    left = 1
    right = max(times) * n
    answer = right

    while left <= right:
        mid = (left + right) // 2

        # mid 시간 동안 처리 가능한 총 인원 수
        total = 0
        for t in times:
            total += mid // t

        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
