T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    if n == 1:
        print('0')
    elif n % 2 == 0:
        print('8' * (n // 2))
    else:
        print('4' + '8' * (n // 2))