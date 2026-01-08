N, M = map(int, input().split())
costs = [int(input()) for _ in range(N)]
left = max(costs)
right = sum(costs)
answer = right

def count_withdrawals(K):
    """인출 금액 K로 N일을 버티기 위해 필요한 인출 횟수를 구하는 함수"""
    cnt = 1        # 처음에 한 번 인출
    money = K

    for c in costs:
        if money < c:   # 오늘 쓸 돈이 모자라면 새로 인출
            cnt += 1
            money = K
        money -= c      # 오늘 사용
    return cnt

while left <= right:
    mid = (left + right) // 2  # 후보 K

    if count_withdrawals(mid) <= M:
        # M번 이내로 가능 → 더 줄일 수 있는지 왼쪽 구간 탐색
        answer = mid
        right = mid - 1
    else:
        # 인출 횟수가 M보다 많다 → K를 더 크게
        left = mid + 1

print(answer)
