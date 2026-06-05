from math import isqrt

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    S, P = map(int, input().split())    # x - Sx + P = 0 이차방정식의 해(N, M), x = S +- sqrt(S^2 - 4P) // 2

    D = S * S - 4 * P   # b^2 - 4ac 판별식
    exist = False

    if D >= 0:
        r = isqrt(D)            # 정수 제곱근
        if r * r == D and (S - r) % 2 == 0:
            N = (S - r) // 2
            M = (S + r) // 2
            if N >= 1 and M >= 1:
                exist = True

    if exist:
        print('Yes')
    else:
        print('No')
