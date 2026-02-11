from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    for start, end in tickets:
        routes[start].append(end)

    for r in routes:
        routes[r].sort(reverse=True)

    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]

        if top in routes and routes[top]:
            stack.append(routes[top].pop())
        else:
            path.append(stack.pop())

    return path[::-1]