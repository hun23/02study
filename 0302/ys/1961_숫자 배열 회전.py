T = int(input())

for tc in range(1, T + 1):
    # 1
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []  # 전체를 모을 리스트

    # 2-1. 90도
    for j in range(n):
        new_arr = []
        for i in range(n-1, -1, -1):
            new_arr.append(arr[i][j])
        result.append(new_arr)

    # 2-2. 180도
    for i in range(n-1, -1, -1):
        new_arr = []
        for j in range(n-1, -1, -1):
            new_arr.append(arr[i][j])
        result.append(new_arr)

    # 2-3. 270도
    for j in range(n-1, -1, -1):
        new_arr = []
        for i in range(n):
            new_arr.append(arr[i][j])
        result.append(new_arr)

    # 3
    # 출력
    print(f'#{tc}')
    for i in range(n):
            print(*result[i], ' ', *result[i + n], ' ', *result[i + (n * 2)], sep='')