T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]  # N * N arr
    for m in range(M):  # for all saek-jong-i
        r, c, clen, rlen = map(int, input().split())
        for r_idx in range(rlen):  # fill arr
            arr[r + r_idx][c: c + clen] = [1] * clen
    sum_ = 0
    for a in arr:  # count filled cells
        sum_ += sum(a)
    print(f"#{tc} {sum_}")
