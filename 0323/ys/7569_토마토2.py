from collections import deque

# 1
# bfs 함수
# 익어가는 초 표시한 tomato return
def bfs():
    while queue:
        x, y, z = queue.popleft()
        # 3차원
        dx = [-1, 1, 0, 0, 0, 0]
        dy = [0, 0, -1, 1, 0, 0]
        dz = [0, 0, 0, 0, -1, 1]

        for k in range(6):
            sx = x + dx[k]
            sy = y + dy[k]
            sz = z + dz[k]

            if 0 <= sx < h and 0 <= sy < n and 0 <= sz < m and tomato[sx][sy][sz] == 0:
                queue.append([sx, sy, sz])
                tomato[sx][sy][sz] = tomato[x][y][z] + 1  # 1 더해서 익음 표시
    return tomato

# 2
m, n, h = map(int, input().split())  # 상자 크기, 상자 수
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]  # 3차원 배열

# 2-2
# 익은 토마토 찾기
queue = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append([i, j, k])

# 3. 결과 출력
tomato = bfs()
tomatoss = sum(sum(tomato, []), []) # 3차원 -> 1차원

if 0 in tomatoss:
    print(-1)
elif 2 in tomatoss:  # 2가 있다면 normal한 방식
    print(max(tomatoss) - 1)
else:
    print(0)