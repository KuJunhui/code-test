def solution(msg: str):
    # 1) 사전 초기화: 'A'~'Z' -> 1~26
    dic = {chr(ord('A') + i): i + 1 for i in range(26)}
    next_idx = 27

    answer = []
    i = 0
    n = len(msg)

    while i < n:
        # 2) 사전에 있는 가장 긴 문자열 w 찾기
        w = msg[i]
        j = i + 1
        while j <= n and msg[i:j] in dic:
            w = msg[i:j]
            j += 1
        # 3) w의 색인 출력
        answer.append(dic[w])

        # 4) 다음 글자가 남아있으면 w+c 사전에 추가
        if i + len(w) < n:
            wc = msg[i:i + len(w) + 1]
            if wc not in dic:
                dic[wc] = next_idx
                next_idx += 1

        # 5) 입력에서 w 제거 (포인터 이동)
        i += len(w)

    return answer
