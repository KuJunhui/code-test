import heapq

def solution(operations):
    heap = []
    for operation in operations:
        op, num = operation.split()
        if op == 'I':
            heapq.heappush(heap, int(num))
        elif op == 'D' and heap:
            if num == '1':
                heap.remove(max(heap))
            elif num == '-1':
                heapq.heappop(heap)

    answer = [0, 0]
    if heap:
        answer[0] = max(heap)
        answer[1] = min(heap)
        return answer
    else:
        return answer