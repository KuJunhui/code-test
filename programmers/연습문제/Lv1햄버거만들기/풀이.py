def solution(ingredient):
    stack = []
    count = 0

    for i in ingredient:
        stack.append(i)
        # 스택의 위 4개가 [1, 2, 3, 1] 패턴인지 확인
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            # 햄버거 완성! 4개 제거
            for _ in range(4):
                stack.pop()
            count += 1

    return count
