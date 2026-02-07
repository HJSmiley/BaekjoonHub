from collections import deque

def normalize(shape):
    if not shape:
        return []

    min_y = min(c[0] for c in shape)
    min_x = min(c[1] for c in shape)

    return sorted([(y - min_y, x - min_x) for y, x in shape])

def extract_shapes(board, target_val):
    n = len(board)
    visited = [[False for _ in range(n)] for _ in range(n)]
    shapes = []

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == target_val:
                visited[i][j] = True
                q = deque([(i, j)])
                raw_shape = [(i, j)]

                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        ny, nx = y + dy[k], x + dx[k]
                        if 0 <= ny < n and 0 <= nx < n:
                            if not visited[ny][nx] and board[ny][nx] == target_val:
                                visited[ny][nx] = True
                                q.append((ny, nx))
                                raw_shape.append((ny, nx))

                shapes.append(normalize(raw_shape))
    return shapes

def rotate(shape):
    rotated = [(x, -y) for y, x in shape]
    return normalize(rotated)

def solution(game_board, table):
    answer = 0
    pieces = extract_shapes(table, 1)
    blanks = extract_shapes(game_board, 0)

    for blank in blanks:
        matched = False
        
        for i, piece in enumerate(pieces):
            if piece is None:
                continue
            if len(blank) != len(piece):
                continue

            for _ in range(4):
                piece = rotate(piece)
                if blank == piece:
                    answer += len(blank)
                    pieces[i] = None
                    matched = True
                    break

            if matched:
                break

    return answer