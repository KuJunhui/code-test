from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    cache = deque()
    time = 0

    for city in cities:
        city = city.lower()

        if city in cache:          # hit
            time += 1
            cache.remove(city)     # 기존 위치 제거 후
            cache.append(city)     # 최근 사용으로 맨 뒤에
        else:                      # miss
            time += 5
            if len(cache) == cacheSize:
                cache.popleft()    # LRU 제거
            cache.append(city)     # 새 항목을 MRU로

    return time
