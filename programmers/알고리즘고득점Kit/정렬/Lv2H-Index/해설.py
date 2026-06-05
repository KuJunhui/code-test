def solution(citations):
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations):
        # i+1편째 논문이고, 그 논문의 인용 횟수가 c
        # h = i+1 일 때, 인용 횟수가 (i+1) 이상인 논문이 (i+1)편 이상인지 확인
        if c >= i + 1:
            h = i + 1
        else:
            break
    return h
