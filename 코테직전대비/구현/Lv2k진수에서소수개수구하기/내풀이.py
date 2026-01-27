import numpy as np

def solution(n, k):
    base_k = np.base_repr(n, base=k)
    lst = base_k.split('0')
    answer = 0

    for num in lst:
        if num != '':
            if is_prime(int(num)):
                answer += 1

    return answer

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n > 2:
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
    return True

print(solution(437674, 3))
