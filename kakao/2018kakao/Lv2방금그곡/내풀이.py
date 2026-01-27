def solution(m, musicinfos):
    def normalize(s: str) -> str:
        return (s.replace('C#', 'c')
                .replace('D#', 'd')
                .replace('F#', 'f')
                .replace('G#', 'g')
                .replace('A#', 'a'))

    def to_minutes(hhmm: str) -> int:
        hh, mm = hhmm.split(':')
        minutes = int(hh)*60 + int(mm)
        return minutes

    m = normalize(m)
    title_final = '(None)'
    dur_min_final = -1
    order_final = 100

    for idx, info in enumerate(musicinfos):
        s_t, e_t, title, note = info.split(',')
        dur_min = to_minutes(e_t) - to_minutes(s_t)
        note = normalize(note)
        play_note = note*(dur_min//len(note)) + note[:dur_min%len(note)]

        if m in play_note:
            if dur_min > dur_min_final or (dur_min == dur_min_final and idx < order_final):
                title_final = title
                dur_min_final = dur_min
                order_final = idx

    return title_final
