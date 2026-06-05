T = int(input())

for test_case in range(1, T + 1):
    H = 998_244_353
    a, b, c = map(int, input().split())

    a_sum = ((1 + a) * a) // 2
    b_sum = ((1 + b) * b) // 2
    c_sum = ((1 + c) * c) // 2

    print((a_sum * b_sum * c_sum) % H)
