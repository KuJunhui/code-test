import heapq


def solution(scoville, K):
    heapq.heapify(scoville)  # 최소 힙(Heap) 생성
    mix_count = 0

    while scoville:
        min_spicy = heapq.heappop(scoville)  # 가장 작은 값

        # 모든 음식이 K 이상이면 종료
        if min_spicy >= K:
            return mix_count

        # 더 이상 섞을 음식이 없으면 불가능
        if not scoville:
            return -1

        second_spicy = heapq.heappop(scoville)
        new_spicy = min_spicy + (second_spicy * 2)
        heapq.heappush(scoville, new_spicy)

        mix_count += 1

    return -1
