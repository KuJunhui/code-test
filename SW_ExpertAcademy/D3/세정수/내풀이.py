T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    X, Y, Z = map(int, input().split())

    if X == Y and Z <= X:
        print(Z, X, Z)
    elif X == Z and Y <= X:
        print(X, Y, Y)
    elif Y == Z and X <= Y:
        print(X, X, Y)
    else:
        print('-1 -1 -1')