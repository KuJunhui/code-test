def solution(m, musicinfos):
    # 샾 음을 단일 문자로 치환 (오탐 방지)
    def normalize(s: str) -> str:
        return (s.replace("C#", "c")
                 .replace("D#", "d")
                 .replace("F#", "f")
                 .replace("G#", "g")
                 .replace("A#", "a"))

    def to_minutes(hhmm: str) -> int:
        h, mm = hhmm.split(":")
        return int(h) * 60 + int(mm)

    m = normalize(m)

    best_title = "(None)"
    best_playtime = -1
    best_idx = 10**9

    for idx, info in enumerate(musicinfos):
        start, end, title, sheet = info.split(",")
        playtime = to_minutes(end) - to_minutes(start)

        sheet = normalize(sheet)

        # 실제 재생 멜로디 만들기 (1분에 1음)
        if len(sheet) >= playtime:
            played = sheet[:playtime]
        else:
            q, r = divmod(playtime, len(sheet))
            played = sheet * q + sheet[:r]

        # 멜로디 포함 여부 체크
        if m in played:
            # 가장 긴 재생시간 우선, 동률이면 먼저 입력된 곡
            if playtime > best_playtime or (playtime == best_playtime and idx < best_idx):
                best_playtime = playtime
                best_title = title
                best_idx = idx

    return best_title
