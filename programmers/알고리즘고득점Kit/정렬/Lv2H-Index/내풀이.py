def solution(citations):
    citations.sort()
    n = len(citations)

    left, right = 0, n
    answer = right
    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        for c in citations:
            if c >= mid:
                cnt += 1

        if cnt >= mid:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
