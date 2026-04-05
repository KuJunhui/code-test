N, K = map(int, input().split())
a = [0] + [int(input()) for _ in range(N)]  # 1-indexed
total = sum(a)

if K == N:
    print(total)
    exit()

INF = float('inf')
dp = [INF] * (N + 1)
for i in range(1, N + 1):
    # i번을 첫 번째 빈칸으로 고르는 경우
    if i <= K + 1:
        dp[i] = a[i]
# i - j - 1 <= K
    # 이전 빈칸 j를 하나 골라서 이어붙이기
    for j in range(max(1, i - (K + 1)), i):
        dp[i] = min(dp[i], dp[j] + a[i])

# 마지막 빈칸은 뒤쪽에 K개 이하가 남도록 N-K ~ N 사이에 있어야 함
min_removed = min(dp[max(1, N - K):N + 1])

print(total - min_removed)
