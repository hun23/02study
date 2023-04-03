T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

# dfs =====================================

    def dfs(x, y, route, item):

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        # global 변수 선언 필요
        global ans
        if route > ans:
            ans = route

        visited[x][y] = 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # (1) 공사가 필요 없는 곳으로 이동시
                if arr[x][y] > arr[nx][ny]:
                    dfs(nx, ny, route + 1, item)
                # (2) 공사가 필요한/의미 있는 곳으로 이동시
                elif arr[nx][ny] - k < arr[x][y] and item:
                    tmp = arr[nx][ny]
                    arr[nx][ny] = arr[x][y] - 1  # 공사한 상황을 가정
                    dfs(nx, ny, route + 1, False)
                    arr[nx][ny] = tmp  # 공사하기 전으로 값 복귀

        visited[x][y] = 0  # 재방문이 가능하도록 초기화

# =========================================

    maxV = max(sum(arr, [])) # 가장 높은 봉우리
    ans = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == maxV:
                dfs(i, j, 1, True)

    print(f'#{tc} {ans}')
