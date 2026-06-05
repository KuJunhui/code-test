T = int(input())

for test_case in range(1, T + 1):
    s = input()

    has_N = 'N' in s
    has_S = 'S' in s
    has_E = 'E' in s
    has_W = 'W' in s

    if has_N != has_S:
        print('No')
    elif has_E != has_W:
        print('No')
    else:
        print('Yes')
