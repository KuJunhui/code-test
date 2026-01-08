def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        row = bin(arr1[i] | arr2[i])[2:]
        row = row.zfill(n)
        row = row.replace("1", "#").replace("0", " ")
        answer.append(row)

    return answer
