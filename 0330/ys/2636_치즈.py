
from collections import deque

# 1
# 공기의 좌표를 기준으로 bfs 탐색하여 녹일 치즈를 melt에 넣고 반환 -> melt를 queue에 넣어서 계속 돌리기
def bfs(queue):
    melt = deque([])  # 녹일 치즈
    visited = [[0] * m for _ in range(n)]

    while queue:
        x, y = queue.popleft()

        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)): # 4방향 탐색
            i, j = x + di, y + dj
            # 1) 공기라면 -> queue에 추가
            if 0 <= i < n and 0 <= j < m and cheese[i][j] == 0 and visited[i][j] == 0:
                visited[i][j] = 1
                queue.append([i, j])
            # 2) 녹일 치즈라면 -> melt에 추가
            elif 0 <= i < n and 0 <= j < m and cheese[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                melt.append([i, j])

    # 1-3 치즈 녹이기
    for l in melt:
        cheese[l[0]][l[1]] = 0

    return melt


# 2-1 초기 설정
n, m = map(int, input().split()) # 세로, 가로
cheese = [list(map(int, input().split())) for _ in range(n)]

queue = deque([(0, 0)])  # 0, 0에서 bfs 시작
c_left = [] # 녹는 치즈의 개수 lst
cnt = 0 # 시간

# 2-2 함수 시작
while True:
    queue = bfs(queue)

    if len(queue) == 0:  # queue의 길이가 0이면 종료
        print(cnt)
        print(c_left[-1]) # 마지막 녹일 치즈의 개수 출력
        break
    else:
        cnt += 1
        c_left.append(len(queue)) # 녹일 치즈의 개수 더하기