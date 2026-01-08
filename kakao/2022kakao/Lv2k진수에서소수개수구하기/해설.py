import numpy as np


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    # 1. k진수 변환
    base_k = np.base_repr(n, base=k)

    # 2. 0으로 분리
    candidates = base_k.split('0')

    # 3. 소수 판별 및 개수 카운트
    count = 0
    print(candidates)
    for c in candidates:
        if c != '':  # 빈 문자열 제외
            num = int(c)
            if is_prime(num):
                count += 1
    return count

print(solution(437674, 3))