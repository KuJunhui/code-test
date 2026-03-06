import heapq


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while 1:
        first_food = heapq.heappop(scoville)
        if first_food >= K:
            break
        if not scoville:
            count = -1
            break
        second_food = heapq.heappop(scoville)
        new_food = first_food + second_food * 2
        heapq.heappush(scoville, new_food)
        count += 1
    # print(count)
    # print(scoville)

    return count