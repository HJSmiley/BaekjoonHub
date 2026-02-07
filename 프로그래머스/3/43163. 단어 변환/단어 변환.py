from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    q = deque([(begin, 0)])

    visited = set([begin])

    while q:
        curr_word, depth = q.popleft()

        if curr_word == target:
            return depth

        for next_word in words:
            if next_word not in visited:
                diff_count = 0
                for a, b in zip(curr_word, next_word):
                    if a != b:
                        diff_count += 1

                if diff_count == 1:
                    visited.add(next_word)
                    q.append((next_word, depth + 1))

    return 0