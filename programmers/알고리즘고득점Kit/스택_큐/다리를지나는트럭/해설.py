from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)  # 다리 상태(트럭 무게 or 0)
    current_weight = 0
    time = 0
    waiting = deque(truck_weights)

    while waiting:
        time += 1

        # 1) 한 칸 전진: 맨 앞이 빠져나감
        out = bridge.popleft()
        current_weight -= out

        # 2) 다음 트럭을 올릴 수 있으면 올림
        if current_weight + waiting[0] <= weight:
            t = waiting.popleft()
            bridge.append(t)
            current_weight += t
        else:
            bridge.append(0)

    # 마지막 트럭이 다리에서 빠져나가는 시간 추가
    return time + bridge_length
