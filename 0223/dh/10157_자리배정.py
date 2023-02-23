C, R = map(int, input().split())
K = int(input())
arr = [[0] * C for _ in range(R)]

if K > C * R:
    print(0)
    exit()

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
n = 1
r, c = R - 1, 0
d = 0
while n <= C * R:
    arr[r][c] = n
    if n == K:
        print(c + 1, R - r)
        exit()
    n += 1
    nr = r + dr[d % 4]
    nc = c + dc[d % 4]
    if not (R > nr >= 0 and C > nc >= 0) or arr[nr][nc] != 0:
        d += 1
        nr = r + dr[d % 4]
        nc = c + dc[d % 4]
    r = nr
    c = nc
