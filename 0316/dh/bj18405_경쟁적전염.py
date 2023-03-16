from collections import deque


def bfs():
    # BFS
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if arr[nr][nc] == 0:
                if time_passed[r][c] + 1 <= S:  # cut when time is over
                    arr[nr][nc] = arr[r][c]
                    time_passed[nr][nc] = time_passed[r][c] + 1
                    q.append((nr, nc))
                    

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# delta
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# put virus coordinates in queue
q = deque()
time_passed = [[-1] * N for _ in range(N)]
for k in range(1, K + 1):
    viruses = [(r, c) for r in range(N) for c in range(N) if arr[r][c] == k]
    for vir in viruses:
        q.append(vir)
        time_passed[vir[0]][vir[1]] = 0

bfs()
print(arr[X - 1][Y - 1])
