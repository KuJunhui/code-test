from math import sqrt

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    S, P = map(int, input().split())
    # x - Sx + P = 0  (N + M = S, N * M = P)
    # S +- sqrt(S^2 - 4*P) // 2
    D = (S**2 - 4*P)
    exist = False

    if D >= 0:
        r = int(sqrt(D))
        if r * r == D and (S + r) % 2 == 0:
            N = (S + r) // 2
            M = (S - r) // 2
            if N >= 1 and M >= 1:
                exist = True

    if exist:
        print('Yes')
    else:
        print('No')
