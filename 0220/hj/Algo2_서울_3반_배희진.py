T = int(input())

for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    x = 0
    y = 0
    visited = [[0]*N for _ in range(N)] # 중복 방문을 막기 위해, 지나간 곳은 1로 표시할 배열 선언
    ans = [arr[x][y]] # 지나온 곳의 값을 저장할 리스트


    while True:
        # 인덱스 범위를 벗어났거나, 이미 지나간 곳에 도달할 경우 break
        if x >= N or y >= N or x < 0 or y < 0 or visited[x][y] == 1:
            break
        ans.append(arr[x][y]) # 지나온 곳의 값을 저장
        if arr[x][y] == 0:
            visited[x][y] = 1 # 방문 표시
            y += 1 # 오른쪽으로 이동
        elif arr[x][y] == 1:
            visited[x][y] = 1 # 방문 표시
            x += 1 # 아래쪽으로 이동
        elif arr[x][y] == 2:
            visited[x][y] = 1 # 방문 표시
            y -= 1 # 왼쪽으로 이동
        elif arr[x][y] == 3:
            visited[x][y] = 1 # 방문 표시
            x -= 1 # 위쪽으로 이동

    # 같은 방향으로 2번 이상 이동할 시 중복된 방향 제거
    i = 0
    while True:
        if i == len(ans)-1:
            break
        if ans[i] == ans[i+1]:
            del ans[i+1]
            continue
        i += 1

    print(f'#{tc}', end =' ')
    print(*ans)