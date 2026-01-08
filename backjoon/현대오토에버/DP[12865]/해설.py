N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]  # (W, V)

# dp[w] = 무게 w까지 담을 때 얻을 수 있는 최대 가치
dp = [0] * (K + 1)

for w, v in items:
    # 같은 물건을 두 번 쓰지 않기 위해 뒤에서 앞으로 순회
    for cur_w in range(K, w - 1, -1):
        dp[cur_w] = max(dp[cur_w], dp[cur_w - w] + v)

print(dp[K])
