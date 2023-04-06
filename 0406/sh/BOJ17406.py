import copy

# 2차원 배열 시계방향으로 회전하는 함수
def rotate(arr, r, c, s):
    # (r-s, c-s)부터 (r+s, c+s)까지의 사각형을 회전
    for i in range(1, s+1):
        temp = arr[r-i][c-i]
        for j in range(r-i+1, r+i+1):
            arr[j-1][c-i] = arr[j][c-i]
        for j in range(c-i+1, c+i+1):
            arr[r+i][j-1] = arr[r+i][j]
        for j in range(r+i-1, r-i-1, -1):
            arr[j+1][c+i] = arr[j][c+i]
        for j in range(c+i-1, c-i-1, -1):
            arr[r-i][j+1] = arr[r-i][j]
        arr[r-i][c-i+1] = temp

# 배열의 합계 중 최솟값을 구해야 하므로 
def minsum(arr):
    return min([sum(row) for row in arr])

# DFS를 이용해 모든 가능한 회전 연산을 수행하는 함수
def dfs(arr, cycle, visited, n, m, k):
    global ans
    if k == len(cycle):
        # 모든 회전 연산을 수행한 경우, 배열의 합계를 계산하고 최소값을 갱신
        ans = min(ans, minsum(arr))
        return
    for i in range(len(cycle)):
        if not visited[i]:
            visited[i] = 1
            # 배열을 복사한 후 회전 연산을 수행하고 DFS 탐색
            temp = copy.deepcopy(arr)
            r, c, s = cycle[i]
            rotate(temp, r-1, c-1, s)
            dfs(temp, cycle, visited, n, m, k+1)
            visited[i] = 0

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cycle = [list(map(int, input().split())) for _ in range(k)]

visited = [0] * k
ans = float('inf')  # 무한대 표시라고 함. (큰 수 입력할 때 용이할듯)
dfs(arr, cycle, visited, n, m, 0)
print(ans)
