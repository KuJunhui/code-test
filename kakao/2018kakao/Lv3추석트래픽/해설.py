def solution(lines):
    def to_ms(time_str: str) -> int:
        # "hh:mm:ss.sss" -> 밀리초 정수
        hh, mm, ss = time_str.split(":")
        s, ms = ss.split(".")
        return (int(hh) * 3600 + int(mm) * 60 + int(s)) * 1000 + int(ms)

    def duration_to_ms(dur_part: str) -> int:
        # "2.0s", "0.351s", "2s" -> ms 정수
        x = dur_part[:-1]  # remove trailing 's'
        if '.' not in x:
            return int(x) * 1000
        a, b = x.split('.')
        b = (b + '00')[:3]  # 소수부를 3자리로 패딩/절단
        return int(a) * 1000 + int(b)

    intervals = []
    for line in lines:
        _, time_part, dur_part = line.split()
        end_ms = to_ms(time_part)
        dur_ms = duration_to_ms(dur_part)
        start_ms = end_ms - dur_ms + 1           # "처리시간은 시작/끝 포함"
        intervals.append((start_ms, end_ms))

    answer = 0
    # 후보 시점: 각 interval의 시작, 끝
    candidates = []
    for s, e in intervals:
        candidates.append(s)
        candidates.append(e)

    # [t, t+999] (포함) 구간에서 겹치는 요청 수를 센다
    for t in candidates:
        t_end = t + 999
        cnt = 0
        for s, e in intervals:
            # 두 구간이 겹치면 카운트
            if s <= t_end and e >= t:
                cnt += 1
        if cnt > answer:
            answer = cnt

    return answer
