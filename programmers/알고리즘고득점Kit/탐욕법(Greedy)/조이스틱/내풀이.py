def solution(name: str) -> int:
    n = len(name)

    # 1) 위/아래(알파벳 변경) 최소 횟수 합
    up_down = 0
    for ch in name:
        diff = ord(ch) - ord('A')
        up_down += min(diff, 26 - diff)

    # 2) 좌/우(커서 이동) 최소 횟수
    # 기본값: 그냥 오른쪽으로 끝까지 가는 경우
    left_right = n - 1

    for i in range(n):
        # i 다음부터 연속된 'A' 구간의 끝 j 찾기
        j = i + 1
        while j < n and name[j] == 'A':
            j += 1

        # 두 가지 방향 전환 케이스를 비교
        #  - 오른쪽으로 i까지 갔다가 되돌아가서(왼쪽) 끝쪽으로 가는 방식
        #  - 끝쪽(오른쪽)으로 갔다가 되돌아와서 i까지 처리하는 방식
        left_right = min(
            left_right,
            2 * i + (n - j),      # i까지 갔다가 뒤로 돌아가기
            i + 2 * (n - j)       # 끝까지 쪽 먼저 갔다가 돌아오기
        )

    return up_down + left_right

# 1 2