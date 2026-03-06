def solution(array, commands):
    answer = []
    for i, j, k in commands:
        sliced_array = array[i - 1:j]
        answer.append(sorted(sliced_array)[k - 1])
    # print(answer)

    return answer