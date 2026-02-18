def solution(progresses, speeds):
    dur_days = []
    for p, s in zip(progresses, speeds):
        remain = 100 - p
        dur = (remain + s - 1) // s
        dur_days.append(dur)

    answer = []
    release_cnt = 1
    last_dur = dur_days[0]
    for d in dur_days[1:]:
        if d <= last_dur:
            release_cnt += 1
        else:
            answer.append(release_cnt)
            release_cnt = 1
            last_dur = d
    answer.append(release_cnt)

    return answer
