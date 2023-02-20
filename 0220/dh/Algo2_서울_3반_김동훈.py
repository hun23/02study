T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    # arr 0 1 2 3 to delta "right - down - left - up"
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    answers = [arr[0][0]]  # first cell
    r, c = 0 + dr[arr[0][0]], 0 + dc[arr[0][0]]  # first move

    while True:
        # check out of index
        if not (N > r >= 0 and N > c >= 0):
            break
        # when cell is visited
        if visited[r][c]:
            break
        # update visited, answer, r, c
        visited[r][c] = True
        d = arr[r][c]  # direction
        if answers[-1] != d:
            answers.append(d)
        r, c = r + dr[d], c + dc[d]  # next r, c
    print(f"#{tc} ", end="")
    print(*answers, sep=" ")
