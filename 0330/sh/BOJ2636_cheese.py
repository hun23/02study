import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]  # 델타
dy = [0, 0, -1, 1]

def bfs(a, b):
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append((a, b))         #(a,b)에서 시작
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for i in range(4):       # 상하좌우로 이동하며 그래프 값 변경
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:   # 범위 밖은 빼자
                if visited[nx][ny] == False: 
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        visited[nx][ny] = True
                        continue
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append((nx, ny))

def check():
    cnt = 0         # 치즈가 남아있으면 cnt +=1   
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += 1
    return cnt


time = 0           # 걸린 시간
last_cheese = 0    # 마지막 전까지 안녹은 치즈

while True:
    cheese = check()       # 치즈가 다 녹을때까지
    if cheese > 0:
        bfs(0, 0)
        time += 1          # 걸린 시간과
        last_cheese = cheese    # 안녹은 치즈 개수 출력
    elif cheese == 0:
        break

print(time)
print(last_cheese)