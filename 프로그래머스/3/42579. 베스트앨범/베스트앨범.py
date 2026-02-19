from collections import defaultdict

def solution(genres, plays):
    answer = []
    dt = defaultdict(list)
    n = len(genres)
    
    for i in range(n):
        dt[genres[i]].append((plays[i], i))

    tmp = []
    for k in dt.keys():
        dt[k].sort(key=lambda x: (-x[0], x[1]))
        tmp.append((sum(dt[k][i][0] for i in range(len(dt[k]))), dt[k]))
    
    tmp.sort(key=lambda x: -x[0])

    for t in tmp:
        songs = t[1]
        if len(songs) == 1:
            answer.append(songs[0][1])
        else:
            answer.append(songs[0][1])
            answer.append(songs[1][1])

    return answer