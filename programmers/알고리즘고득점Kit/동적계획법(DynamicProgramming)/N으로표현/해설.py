# d[1] = {5}
# d[2] = {55, 5 + 5, 5 - 5, 5 / 5, 5 * 5}
# dp[i]는 dp[j]와 dp[i-j]의 모든 조합으로 구성

def solution(N, number):
    if N == number:
        return 1

    dp = [set() for _ in range(9)]  # dp[0]은 사용 안 함 (1~8)

    for i in range(1, 9):
        # N, NN, NNN... 형태 숫자 추가
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

print(solution(5, 12))