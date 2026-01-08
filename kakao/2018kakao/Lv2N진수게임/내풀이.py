import numpy as np

def solution(n, t, m, p):
    s = ''
    i = 0
    while i <= t*m - (m-p):
        if i < 2:
            s += str(i)
            i += 1
        else:
            base_k = np.base_repr(i, base=n)
            s += base_k
            i += 1

    answer = ''
    for a in range(p - 1, len(s), m):
        answer += s[a]
        if len(answer) == t:
            return answer
