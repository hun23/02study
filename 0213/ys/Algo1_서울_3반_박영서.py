T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [[0] * n for _ in range(n)]  # n*n
    cnt = 0
    for _ in range(m):  # m개 도장 받기
        x, y, a, b = map(int, input().split())

        for i in range(y, y + a):
            for j in range(x, x + b):
                if arr[i][j] == 0:  # arr가 0으로 표시되었다면,
                    arr[i][j] = 1   # 해당 arr에 1 추가/ 다른 도장이 이미 찍혀있을때 넘어간다.
                    cnt += 1        # 도장을 찍었다면 cnt에 1 추가

    print(f'#{tc} {cnt}')







