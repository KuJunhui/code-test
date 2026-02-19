from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    weights = deque(truck_weights)
    time = 0
    cur_weight = 0

    while weights:
        time += 1
        out = bridge.popleft()
        cur_weight -= out

        if cur_weight + weights[0] <= weight:
            w = weights.popleft()
            bridge.append(w)
            cur_weight += w
        else:
            bridge.append(0)

    return time + bridge_length
