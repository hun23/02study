from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
sr, sc = divmod(sum(arr, []).index(9), N)
arr[sr][sc] = 0
size = 2
cnt = 0

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
answer = 0

while True:
    cnt_before = cnt
    visited = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 0
    can_eat = []
    can_eat_len = 2147483647
    while q:
        r, c = q.popleft()
        if visited[r][c] > can_eat_len:
            break
        if 0 < arr[r][c] < size:
            can_eat.append((r, c))
            can_eat_len = visited[r][c]
            # answer += visited[r][c]
            # arr[r][c] = 0
            # cnt += 1
            # if cnt == size:
            #     size += 1
            #     cnt = 0
            # sr, sc = r, c
            # break
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (N > nr >= 0 and N > nc >= 0):
                continue
            if visited[nr][nc] == -1 and arr[nr][nc] <= size:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
    can_eat.sort()
    # print(f"caneat: {can_eat}")
    if len(can_eat) != 0:
        sr, sc = can_eat[0][0], can_eat[0][1]
        arr[sr][sc] = 0
        cnt += 1
        if cnt == size:
            size += 1 
            cnt = 0
        answer += can_eat_len
    else:
        break

    # for a in arr:
    #     print(a)
    # print(f"cur:{r} {c}, size:{size}, cnt:{cnt}, answer:{answer}")

    if cnt == cnt_before:
        break
print(answer)
