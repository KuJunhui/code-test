def solution(numbers):
    str_n = list(map(str, numbers))
    str_n.sort(key=lambda x: x * 3, reverse=True)
    return '0' if str_n[0] == '0' else ''.join(str_n)
