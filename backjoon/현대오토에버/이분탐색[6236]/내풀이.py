N, M = map(int, input().split())
daily_spend = [int(input()) for _ in range(N)]
left = max(daily_spend)
right = sum(daily_spend)
answer = right

def count_get(K):
    temp_k = K
    cnt = 1
    for amount in daily_spend:
        if temp_k < amount:
            cnt += 1
            temp_k = K - amount
        else:
            temp_k -= amount
    return cnt

while left <= right:
    mid = (left + right) // 2
    m = count_get(mid)
    if m <= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)