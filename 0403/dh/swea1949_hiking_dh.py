def dfs(v, r, c, leng, cut):
    global max_len

    if v[r][c]:
        return
    v[r][c] = True
    if leng > max_len:
        max_len = leng

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if not (N > nr >= 0 and N > nc >= 0):
            continue
        if arr[nr][nc] < arr[r][c]:
            dfs(v, nr, nc, leng + 1, cut)
        elif not cut:  # cut if possible
            diff = arr[nr][nc] - arr[r][c]
            if diff < K:
                arr[nr][nc] -= (1 + diff)
                dfs(v, nr, nc, leng + 1, True)
                arr[nr][nc] += (1 + diff)
    v[r][c] = False


T = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # get start point
    max_height = max(sum(arr, []))
    starts = [(r, c) for r in range(N) for c in range(N) if arr[r][c] == max_height]

    max_len = 0
    for r, c in starts:
        visited = [[False] * N for _ in range(N)]
        dfs(visited, r, c, 1, False)

    print(f"#{tc} {max_len}")
