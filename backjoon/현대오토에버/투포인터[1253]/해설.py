# 투 포인터
N = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0

for i in range(N):
    target = A[i]
    left, right = 0, N - 1

    # 투 포인터로 A[left] + A[right] == target 찾기
    while left < right:
        # 검사 대상(target)은 건너뛰기
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue

        s = A[left] + A[right]
        if s == target:
            count += 1
            break
        elif s < target:    # 합 키우기
            left += 1
        else:               # 합 줄이기
            right -= 1

print(count)
