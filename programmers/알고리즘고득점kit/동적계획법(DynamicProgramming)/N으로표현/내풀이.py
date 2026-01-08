# dp[1] = {5}
# dp[2] = {55, 5 + 5, 5 - 5, 5 * 5, 5 // 5}
# dp[i]는 dp[j]와 dp[i-j]의 모든 조합

def solution(N, number):
    if N == number:
        return 1

    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))

        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
        if number in dp[i]:
            return i

    return -1

print(solution(2, 11))