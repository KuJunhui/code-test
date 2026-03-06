def solution(arr):
    stack = []
    for value in arr:
        # 스택이 비어 있는 경우 -> if not stack
        if not stack or stack[-1] != value:
            stack.append(value)
    return stack