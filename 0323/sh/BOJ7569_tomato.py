from collections import deque

# 입력 받기
M, N, H = map(int, input().split())
boxes = []
for _ in range(H):
    box = []
    for _ in range(N):
        row = list(map(int, input().split()))
        box.append(row)
    boxes.append(box)

# 상하좌우앞뒤 이동을 위한 dx, dy, dz
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

# bfs 함수 정의
def bfs():
    q = deque()
    # 익은 토마토의 위치를 큐에 넣음
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if boxes[i][j][k] == 1:
                    q.append((i, j, k))
    # bfs 탐색 시작
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0<=nx<N and 0<=ny<M and 0<=nz<H and boxes[nz][nx][ny]==0:
                q.append((nz, nx, ny))
                boxes[nz][nx][ny] = boxes[z][x][y] + 1

    # 탐색 후, 모든 토마토가 익었는지 확인
    days = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                # 안익은 토마토가 있다면 -1을 반환
                if boxes[i][j][k] == 0:
                    return -1
                # 그렇지 않다면, 최대 익는 일수를 구함
                days = max(days, boxes[i][j][k])

    # 최대 익는 일수 반환
    return days - 1

# bfs 함수 호출 및 결과 출력
print(bfs())
