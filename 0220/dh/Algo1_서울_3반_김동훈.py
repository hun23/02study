T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bongs = []
    # 8 direction deltas
    dr = [1, -1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, 1, -1, 1, -1, 1, -1]

    # check arr
    for r in range(1, N - 1):
        for c in range(1, N - 1):
            bong = arr[r][c]
            for d in range(8):
                nr, nc = r + dr[d], c + dc[d]
                if arr[nr][nc] >= bong:
                    break
            else:
                bongs.append(bong)

    # check answer
    if len(bongs) <= 1:  # if no bong or just one bong
        answer = -1
    else:
        answer = max(bongs) - min(bongs)
    print(f"#{tc} {answer}")
