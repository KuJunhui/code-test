def solution(genres, plays):
    group = []
    genre_play = {}
    genre_cnt = {}
    n = len(genres)

    for idx, genre in enumerate(genres):
        genre_play[genre] = genre_play.get(genre, 0) + plays[idx]

    for i in range(n):
        group.append((genre_play[genres[i]], plays[i], i, genres[i]))

    group.sort(key=lambda x: (-x[0], -x[1], x[2]))

    answer = []
    for i in range(n):
        genre_cnt[group[i][3]] = genre_cnt.get(group[i][3], 0)
        if genre_cnt[group[i][3]] < 2:
            answer.append(group[i][2])
            genre_cnt[group[i][3]] = genre_cnt.get(group[i][3]) + 1

    return answer
