T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    x, y, ver, hor = list(map(int, input().split()))
    # 도장의 좌측 하단 x, y 좌표, 너비, 높이
    arr = [0]* (N ** 2) # 도화지 넓이

    for _ in range(1, N+1):
        cnt = 0  # 도장이 찍힌 횟수
        for i in range(x, x+ver):  # 도장의 가로
            for j in range(y, y+hor): # 도장의 세로

                cnt += 1

            if i > ver and j > hor:   # 가로 세로 범위를 넘어가면
                break

    print(f'#{test_case} {cnt}')