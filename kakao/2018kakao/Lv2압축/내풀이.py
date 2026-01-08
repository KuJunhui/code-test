def solution(msg):
    dic = {chr(ord('A') + i): i + 1 for i in range(26)}
    next_idx = 27
    answer = []
    n = len(msg)
    i = 0

    while i < n:
        j = i + 1
        w = msg[i:j]
        while j <= n and msg[i:j] in dic:
            w = msg[i:j]
            j += 1
        answer.append(dic[w])

        if i + len(w) < n:
            wc = msg[i:i + len(w) + 1]
            if wc not in dic:
                dic[wc] = next_idx
                next_idx += 1

        i += len(w)

    return answer