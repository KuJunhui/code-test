def solution(numbers):
    strs = list(map(str, numbers))
    strs.sort(key=lambda x: x * 3, reverse=True)
    answer = ''.join(strs)
    return '0' if answer[0] == '0' else answer