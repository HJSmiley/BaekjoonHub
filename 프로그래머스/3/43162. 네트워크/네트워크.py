def solution(n, computers):
    
    def dfs(start):
        s = [start]

        while s:
            node = s.pop()
            if visited[node]:
                continue

            visited[node] = True

            for j in range(n):
                if computers[node][j]:
                    s.append(j)
        return

    answer = 0
    visited = [False] * (n)
    
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer