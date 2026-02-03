def solution(participant, completion):
    d_participant = {}
    d_completion = {}

    for p in participant:
        d_participant[p] = d_participant.get(p, 0) + 1

    for c in completion:
        d_completion[c] = d_completion.get(c, 0) + 1

    for p in participant:
        if p not in d_completion or d_participant[p] > d_completion[p]:
            return p

    return