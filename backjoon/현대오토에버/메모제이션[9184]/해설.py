# dp[a][b][c] 를 저장할 3차원 리스트 (0~20까지 사용)
dp = [[[0] * 21 for _ in range(21)] for __ in range(21)]

def w(a, b, c):
    # 1번 조건
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    # 2번 조건: 20을 넘으면 w(20,20,20)과 같음
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 이미 계산된 값이면 그대로 사용 (메모이제이션)
    if dp[a][b][c] != 0:
        return dp[a][b][c]

    # 3번 조건
    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        # 4번 조건 (otherwise)
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
