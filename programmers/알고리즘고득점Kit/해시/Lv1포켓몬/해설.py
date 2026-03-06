def solution(nums):
    # 전체 포켓몬 중 절반만 선택 가능
    max_pick = len(nums) // 2
    # 중복 제거하여 종류의 수 계산
    unique_types = len(set(nums))
    # 두 값 중 더 작은 값을 반환
    return min(unique_types, max_pick)
