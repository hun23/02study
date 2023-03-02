T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # N을 큰쪽, M을 작은 쪽으로 만들기
    if N > M:
        big = list(map(int, input().split()))
        small = list(map(int, input().split()))
    else:
        N, M = M, N
        small = list(map(int, input().split()))
        big = list(map(int, input().split()))

    # 반복하면서 최대값 찾기
    mx = 0
    for i in range(N - M + 1):
        temp = 0
        for m in range(M):
            temp += big[i + m] * small[m]
        if temp > mx:
            mx = temp
    print(f"#{tc} {mx}")
