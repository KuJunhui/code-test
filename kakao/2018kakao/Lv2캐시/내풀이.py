from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    cache = deque()
    total_time = 0

    for city in cities:
        if city in cache:
            total_time += 1
            cache.remove(city)
            cache.append(city)
        else:
            total_time += 5
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)

    return total_time
