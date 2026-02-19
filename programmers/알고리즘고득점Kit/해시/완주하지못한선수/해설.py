from collections import Counter


def solution(participant, completion):
    # 각 이름별 등장 횟수 세기
    p_counter = Counter(participant)
    c_counter = Counter(completion)

    # 참가자 - 완주자 차집합 구하기 (Counter 간 뺄셈 가능)
    diff = p_counter - c_counter

    # 남은 키(이름) 반환
    return list(diff.keys())[0]
