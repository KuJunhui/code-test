def solution(genres, plays):
    # 장르별 총 재생 횟수 집계
    genre_total = {}
    # 장르별 (재생 횟수, 고유 번호) 목록
    genre_songs = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total[g] = genre_total.get(g, 0) + p
        genre_songs.setdefault(g, []).append((p, i))

    answer = []

    # 1) 총 재생 횟수가 많은 장르부터 처리
    for g in sorted(genre_total, key=lambda x: genre_total[x], reverse=True):
        # 2) 재생 횟수 많은 순, 같으면 고유 번호 낮은 순
        songs = sorted(genre_songs[g], key=lambda x: (-x[0], x[1]))
        # 3) 최대 두 곡 수록
        for p, i in songs[:2]:
            answer.append(i)

    return answer