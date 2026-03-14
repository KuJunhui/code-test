def solution(number, k):
    stack = []

    for num in number:
        # 아직 지울 수 있고,
        # 스택 마지막 숫자가 현재 숫자보다 작으면 제거
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    # 아직 k가 남아 있으면 뒤에서 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)
