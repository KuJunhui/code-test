def solution(n, t, m, timetable):
    # "HH:MM" -> minutes
    def to_min(s):
        hh, mm = map(int, s.split(":"))
        return hh * 60 + mm

    # minutes -> "HH:MM"
    def to_hhmm(x):
        hh = x // 60
        mm = x % 60
        return f"{hh:02d}:{mm:02d}"

    crew = sorted(to_min(x) for x in timetable)

    start = 9 * 60  # 09:00
    idx = 0         # crew pointer
    last_boarded_time = None  # 마지막 셔틀에서 마지막으로 탑승한 크루 시간

    for i in range(n):
        shuttle_time = start + i * t
        cnt = 0

        # 이번 셔틀에 탈 수 있는 크루들 태우기 (최대 m명)
        while cnt < m and idx < len(crew) and crew[idx] <= shuttle_time:
            last_boarded_time = crew[idx]
            idx += 1
            cnt += 1

        # 마지막 셔틀에서 답 결정
        if i == n - 1:
            if cnt < m:
                # 자리 남음: 콘은 셔틀 도착 시간에 와도 탑승 가능
                return to_hhmm(shuttle_time)
            else:
                # 자리 꽉 참: 콘은 마지막으로 탄 크루보다 1분 빨리 와야 함
                return to_hhmm(last_boarded_time - 1)