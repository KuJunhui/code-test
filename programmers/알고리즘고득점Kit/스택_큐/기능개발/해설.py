def solution(progresses, speeds):
    answer = []

    # 1) 완료까지 걸리는 일수 계산 (ceil 직접 구현)
    days = []
    for p, s in zip(progresses, speeds):
        remain = 100 - p
        d = (remain + s - 1) // s  # ceil(remain / s)
        days.append(d)

    # 2) 배포 묶기
    current_release_day = days[0]
    count = 1

    for d in days[1:]:
        if d <= current_release_day:
            count += 1
        else:
            answer.append(count)
            current_release_day = d
            count = 1

    answer.append(count)
    return answer
