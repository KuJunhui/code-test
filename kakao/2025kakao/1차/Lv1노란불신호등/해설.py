from math import gcd

def lcm(a, b): # 최소공배수
    return a * b // gcd(a, b) # 최대공약수

def solution(signals):
    # 전체 반복 주기 구하기
    total_cycle = 1
    for G, Y, R in signals:
        total_cycle = lcm(total_cycle, G + Y + R)

    # 1초부터 전체 반복 주기까지 확인
    for t in range(1, total_cycle + 1):
        all_yellow = True

        for G, Y, R in signals:
            cycle = G + Y + R
            x = (t - 1) % cycle

            # 노란불 구간이 아니면 실패
            if not (G <= x < G + Y):
                all_yellow = False
                break

        if all_yellow:
            return t

    return -1