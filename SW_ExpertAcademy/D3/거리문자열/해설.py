T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s = input()

    def check_s(s):
        numbers = set()
        for n in s:
            numbers.add(n)

        for n in numbers:
            if s.count(n) != 2:
                return False

        visited = []
        for i in range(len(s)):
            ch1 = s[i]
            cnt = 0
            if ch1 not in visited:
                visited.append(ch1)
                for j in range(i + 1, len(s)):
                    if ch1 == s[j] and int(ch1) == cnt:
                        break
                    elif ch1 == s[j] and int(ch1) != cnt:
                        return False
                    cnt += 1
        return True

    if check_s(s):
        print('yes')
    else:
        print('no')