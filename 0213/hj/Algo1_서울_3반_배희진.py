T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    ans = [[0] * N for _ in range(N)]

    for _ in range(M):
        a, b, c, d = map(int, input().split()) # 열, 행, 너비, 높이

        for i in range(b, b+c):
            for j in range(a, a+d):
                ans[i][j] = 1

    sum = 0
    for i in range(N):
        sum += ans[i].count(1) # 1 개수 구하기

    print(f'#{test_case} {sum}')