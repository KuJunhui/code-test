def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        # 1️⃣ i번째부터 j번째까지 자르기 (슬라이싱은 0-index라 i-1부터 j까지)
        sliced = array[i-1:j]
        # 2️⃣ 정렬
        sliced.sort()
        # 3️⃣ k번째 원소 선택 (0-index 보정으로 k-1)
        answer.append(sliced[k-1])
    return answer
