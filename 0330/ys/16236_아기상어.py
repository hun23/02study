
from collections import deque

# 1
# queue에 담긴 아기상어의 위치를 받아 -> 아기상어가 조건에 맞는 물고기를 먹을때의 (걸리는 초, 위치 바꾸는 함수)
# 가장 가까운 물고기 > 가장 위에 있는 물고기 > 가장 왼쪽에 있는 물고기 => 1)fx가 가장 작다, 2)fy가 가장 작다
def bfs(queue):
    # 1-1
    global eat, shark, second, fx, fy, n
    visited = [[0] * (n + 2) for _ in range(n + 2)]
    minfish = n * n  # 최소 거리
    mx, my = n + 2, n + 2 # 최소 거리 좌표

    # 1-2
    while queue:
        x, y = queue.popleft()  # 상어 시작점

        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            i, j = x + di, y + dj

            # 1) 물고기를 먹는 경우 -> 그 중에서 가장 가까운 물고기 > 가장 위에 있는 물고기 > 가장 왼쪽에 있는 물고기
            # 조건에 따라 비교 후 최소 거리, 최소거리 좌표 갱신
            if 0 < sea[i][j] < shark and visited[x][y] + 1 <= minfish: # 최소거리
                if i < mx: # 가장 위쪽
                    mx, my = i, j
                    visited[mx][my] = visited[x][y] + 1
                    minfish = visited[mx][my]
                elif i == mx and j < my: # 가장 왼쪽
                    mx, my = i, j
                    visited[mx][my] = visited[x][y] + 1
                    minfish = visited[mx][my]

            # 2) 아기상어가 이동하는 경우
            elif 0 <= sea[i][j] <= shark and visited[i][j] == 0:
                queue.append([i, j])
                visited[i][j] = visited[x][y] + 1  # 초 표시

            # 3) 이미 먹을 물고기가 정해진 경우 -> 변수 갱신하고 return
            elif visited[x][y] + 1 > minfish:
                sea[mx][my] = 0             # 물고기 먹어서 0으로 변환
                fx, fy = mx, my             # 먹은 물고기 좌표
                second += visited[mx][my]   # second에 걸린 초 더하기
                eat += 1                    # eat + 1
                return

    # 1-3 while문 종료되었는데 return 하지 않았다면
    if minfish == n * n:  # 물고기를 못먹었다 -> 종료
        return False
    else:
        sea[mx][my] = 0
        fx, fy = mx, my
        second += visited[mx][my]
        eat += 1
        return

# 2-1 초기설정
n = int(input())
sea = [[-1] * (n + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(n)] + [[-1] * (n + 2)]

# 2-2 아기상어 위치 찾기
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if sea[i][j] == 9:
            queue = deque([(i, j)])  # 아기상어의 위치를 queue에 넣는다.
            sea[i][j] = 0
            break

# 3-1
# 변수들 설정
second = 0     # 걸리는 시간
eat = 0        # 먹은 물고기 수 -> 크기가 커지면 0으로 갱신
shark = 2      # 아기 상어의 크기
fx, fy = 0, 0  # 먹은 물고기의 위치

# 3-2 함수 시작
# bfs가 False => 더이상 먹을 물고기가 없다 -> second 출력 및 코드 종료
while True:
    rlt = bfs(queue)

    if rlt == False:
        print(second)
        break
    else:
        if eat == shark:
            shark += 1
            eat = 0
        queue = deque([(fx, fy)])  # 먹은 물고기의 위치를 아기상어 위치로 갱신 -> while문 다시 돌기