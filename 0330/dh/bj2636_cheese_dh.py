from collections import deque

N, M = map(int, input().split())  # N, M <= 100
arr = [[0] * M for _ in range(N)]
cheese_cnt = 0
for n in range(N):
    inp = list(map(int, input().split()))
    for m in range(M):
        if inp[m] == 1:
            cheese_cnt += 1
        arr[n][m] = inp[m]

# edge
if cheese_cnt == 0:
    print(0)
    print(0)
    exit()

# delta
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

# BFS start at 0, 0
cycle = 0
cheese_cnts = [cheese_cnt]
while cheese_cnt > 0:
    cycle += 1
    q = deque()
    q.append((0, 0))
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if N > nr >= 0 and M > nc >= 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                if arr[nr][nc] == 1:
                    arr[nr][nc] = 0
                    cheese_cnt -= 1
                else:
                    q.append((nr, nc))
    cheese_cnts.append(cheese_cnt)
    # print(cycle)
    # print(cheese_cnt)
print(cycle)
print(cheese_cnts[-2])
