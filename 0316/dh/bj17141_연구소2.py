from collections import deque

def recursion(start_idx, idx, M, starts, comb):
    if idx == M:
        temp = []
        for c in comb:
            temp.append(starts[c])
        bfs(N, temp)
        return
    for i in range(start_idx, len(starts)):
        comb[idx] = i
        recursion(i + 1, idx + 1, M, starts, comb)
    return

def bfs(N, comb):
    global answer
    global arr
    global dr
    global dc
    q = deque()
    for c in comb:
        q.append(c)
    visited = [[-1] * N for _ in range(N)]
    for r, c in comb:
        visited[r][c] = 0
    while q:
        r, c = q.popleft()
        if visited[r][c] > answer:
            break
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if visited[nr][nc] == -1 and arr[nr][nc] != 1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
    for r in range(N):
        for c in range(N):
            if visited[r][c] == -1 and arr[r][c] != 1:
                return
    temp = max(sum(visited, []))
    if temp < answer:
        answer = temp


N, M = map(int, input().split())
arr = [[0] * N for _ in range(N)]
starts = []
for r in range(N):
    inp = list(map(int, input().split()))
    for c in range(N):
        arr[r][c] = inp[c]
        if inp[c] == 2:
            starts.append((r, c))

# starts 에서 M개 고르기 -> combination(조합, 순서x), permutation(순열, 순서o)
# combination!

# 순열 하나 고르고
# bfs 돌려서 시간 내고
# min값 갱신

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
answer = 2147483647
checked = [False] * len(starts)

recursion(0, 0, M, starts, [-1] * M)
if answer == 2147483647:
    print(-1)
else:
    print(answer)
