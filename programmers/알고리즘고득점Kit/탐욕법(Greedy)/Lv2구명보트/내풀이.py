def solution(people, limit):
    people.sort()

    left = 0
    right = len(people) - 1
    boats = 0

    while left <= right:
        # 가장 가벼운 사람 + 가장 무거운 사람 같이 탈 수 있으면 함께 태움
        if people[left] + people[right] <= limit:
            left += 1

        # 가장 무거운 사람은 항상 이번 보트에 태움
        right -= 1
        boats += 1

    return boats
