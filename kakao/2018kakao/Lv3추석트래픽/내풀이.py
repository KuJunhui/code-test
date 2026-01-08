def solution(lines):
    def to_ms(time_str):
        hh, mm, ss = time_str.split(':')
        s, ms = ss.split('.')
        return (int(hh) * 3600 + int(mm) * 60 + int(s)) * 1000 + int(ms)

    def dur_to_ms(dur_str):
        dur_str = dur_str[:-1]
        if '.' not in dur_str:
            return int(dur_str) * 1000
        s, ms = dur_str.split('.')
        ms = (ms + '00')[:3]
        return int(s) * 1000 + int(ms)

    intervals = []
    candidates = []
    for line in lines:
        _, end_time, dur_time = line.split()
        end_time_ms = to_ms(end_time)
        dur_time_ms = dur_to_ms(dur_time)
        start_time_ms = end_time_ms - dur_time_ms + 1
        intervals.append((start_time_ms, end_time_ms))
        candidates.append(start_time_ms)
        candidates.append(end_time_ms)

    max_cnt = 0
    for t in candidates:
        cnt = 0
        t_end = t + 999
        for s, e in intervals:
            if s <= t_end and e >= t:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

    return max_cnt