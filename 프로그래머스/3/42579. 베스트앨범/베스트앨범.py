from collections import defaultdict


def solution(genres, plays):
    answer = []

    genre_total_plays = defaultdict(int)
    genre_songs = defaultdict(list)

    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total_plays[g] += p
        genre_songs[g].append((p, i))

    sorted_genres = sorted(genre_total_plays.items(), key=lambda x: x[1], reverse=True)

    for g, _ in sorted_genres:
        genre_songs[g].sort(key=lambda x: (-x[0], x[1]))

        answer.extend([idx for _, idx in genre_songs[g][:2]])

    return answer