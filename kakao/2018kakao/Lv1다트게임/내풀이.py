import re

def solution(dartResult):
    # 점수+보너스+옵션 패턴으로 자르기
    rounds = re.findall(r'\d{1,2}[SDT][*#]?', dartResult)
    scores = []

    for i, r in enumerate(rounds):
        # 1. 점수 뽑기
        num = int(re.match(r'\d{1,2}', r).group())

        # 2. 보너스 처리
        if 'S' in r:
            num **= 1
        elif 'D' in r:
            num **= 2
        elif 'T' in r:
            num **= 3

        # 3. 옵션 처리
        if '*' in r:
            num *= 2
            if i > 0:  # 이전 점수도 2배
                scores[i - 1] *= 2
        elif '#' in r:
            num *= -1

        scores.append(num)

    return sum(scores)
