def solution(arr):
    answer = []
    for idx, n in enumerate(arr):
        if idx == 0:
            answer.append(n)
        else:
            if arr[idx] != arr[idx - 1]:
                answer.append(n)

    return answer