from collections import deque

# 1
# 한 좌표에서의 연합
def bfs(x, y):
    # 1-1 초기 설정
    global change

    plus = deque([])  # 연합 o 좌표
    sub = deque([])   # 연합 x 좌표

    p, cnt = 0, 1  # 연합 인구, 연합 나라 수
    p += people[x][y]  # 시작점 인구수 담기
    plus.append([x, y])
    queue = deque([(x, y)])  # 시작점 queue에 넣기

    # 1-2
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1

        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):  # 4방향 탐색
            i, j = x + di, y + dj

            if 0 <= i < n and 0 <= j < n and visited[i][j] == 0:
                # 1) 연합 가능한 나라
                if l <= abs(people[x][y] - people[i][j]) <= r:
                    visited[i][j] = 1
                    queue.append([i, j])  # queue에 좌표 더하기
                    plus.append([i, j])   # 연합 좌표 모으기
                    p += people[i][j]     # 인구 수 +
                    cnt += 1              # 나라 +1

                # 2) 연합 불가능
                elif [i, j] not in sub:
                    sub.append([i, j])

    # 1-3 인구 이동
    if cnt != 1:
        combP = p // cnt  # 연합 인구 수
        change = 1  # 인구 이동이 있었으므로 change -> 1
        for i in plus:  # 인구 이동
            people[i[0]][i[1]] = combP

# 2-1 input
n, l, r = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(n)]
day = 0

# 2-2 함수 시작
while True:

    change = 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0: # 방문하지 않은 좌표에 대해서 bfs
                bfs(i, j)

    if change == 0:  # 더이상 인구 이동이 없다면 -> break
        break
    else:
        day += 1

print(day)