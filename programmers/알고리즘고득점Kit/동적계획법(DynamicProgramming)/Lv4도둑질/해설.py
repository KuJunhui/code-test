def solution(money):
    def rob_linear(arr):
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]

        for x in arr:
            prev2, prev1 = prev1, max(prev1, prev2 + x)

        return prev1

    return max(
        rob_linear(money[:-1]),  # 첫 집 포함 가능, 마지막 집 제외
        rob_linear(money[1:])    # 첫 집 제외, 마지막 집 포함 가능
    )
