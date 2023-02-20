
T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    route = [arr[0][0]]

    i = 0
    j = 0
    while i < n and j < n:
        k = arr[i][j]
        i = i + di[k]
        j = j + dj[k]
        if k < 4:
            if route[-1] != arr[i][j]:  # route의 마지막 값과 다르다면
                route.append(arr[i][j])  # route에 append
                # # arr[i][j] = 4
                # i = i + di[k]
                # j = j + dj[k]

            else:
                continue
                # # arr[i][j] = 4
                # i = i + di[k]
                # j = j + dj[k]

        else:
            break

    print(f'#{tc}', *route)
