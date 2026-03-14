import heapq

def solution(jobs):
    n = len(jobs)

    # (요청시각, 소요시간, 작업번호) 형태로 정리
    arr = [(s, l, i) for i, (s, l) in enumerate(jobs)]
    arr.sort()  # 요청 시각 순 정렬

    heap = []  # (소요시간, 요청시각, 작업번호)
    time = 0  # 현재 시각
    idx = 0  # 아직 heap에 넣지 않은 작업의 인덱스
    total = 0  # 반환 시간 총합

    while idx < n or heap:
        # 현재 시각까지 들어온 작업들을 heap에 모두 넣기
        while idx < n and arr[idx][0] <= time:
            s, l, job_id = arr[idx]
            heapq.heappush(heap, (l, s, job_id))
            idx += 1

        if heap:
            # 우선순위가 가장 높은 작업 선택
            l, s, job_id = heapq.heappop(heap)
            time += l
            total += (time - s)  # 반환 시간 = 종료시각 - 요청시각
        else:
            # 아직 처리할 수 있는 작업이 없으면 다음 작업 요청 시각으로 점프
            time = arr[idx][0]

    return total // n

# 