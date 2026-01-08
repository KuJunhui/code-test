N = int(input())
a_list = list(map(int, input().split()))
a_list.sort()
cnt = 0

for i in range(N):
    target = a_list[i]

    left = 0
    right = N - 1
    while left < right:
        # 검사 대상은 건너뛰기
        if left == i:
            left += 1
            continue
        elif right == i:
            right -= 1
            continue

        s = a_list[left] + a_list[right]
        if s == target:
            cnt += 1
            break
        elif s < target:
            left += 1
        else:
            right -= 1

print(cnt)