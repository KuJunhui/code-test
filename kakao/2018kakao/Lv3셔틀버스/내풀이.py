def solution(n, t, m, timetable):
    def to_min(hhmm: str) -> int:
        hh, mm = hhmm.split(':')
        return int(hh) * 60 + int(mm)

    def to_hhmm(minutes: int) -> str:
        hh = str(minutes // 60).zfill(2)
        mm = str(minutes % 60).zfill(2)
        return hh + ':' + mm

    crew = sorted([to_min(hhmm) for hhmm in timetable])
    idx = 0
    start = to_min('09:00')
    last_ride_time = None

    for i in range(n):
        shuttle_time = start + i * t
        cnt = 0

        while cnt < m and idx < len(crew) and crew[idx] <= shuttle_time:
            last_ride_time = crew[idx]
            idx += 1
            cnt += 1

        if i == n - 1:
            if cnt < m:
                return to_hhmm(shuttle_time)
            else:
                return to_hhmm(last_ride_time - 1)