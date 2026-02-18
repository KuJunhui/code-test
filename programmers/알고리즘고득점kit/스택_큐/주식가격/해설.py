def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []  # 가격이 아직 '떨어진 적 없는' 인덱스들

    for i, p in enumerate(prices):
        # 현재 가격 p가 더 낮아졌다면, 스택의 시점들은 '가격 하락'이 발생한 것
        while stack and prices[stack[-1]] > p:
            j = stack.pop()
            answer[j] = i - j  # j시점 가격은 i에서 떨어짐 (i-j초 동안 안 떨어짐)
        stack.append(i)

    # 끝까지 안 떨어진 애들 처리
    while stack:
        j = stack.pop()
        answer[j] = (n - 1) - j  # 끝 시점까지 유지

    return answer
