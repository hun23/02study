'''
n*n 크기의 시험관
특정한 위치에는 바이러스가 존재할 수 있다.
1~k번 까지의 바이러스

바이러스는 상하좌우 방향으로 증식해 나간다
번호가 낮은 종류의 바이러스부터 먼저 증식한다.

s초가 지난 후에 (x, y)에 존재하는 바이러스의 종류 출력
바이러스가 존재하지 않는다면 0
'''

# 1.
# 상하좌우에 0이 있다면 그 바이러스 숫자 찍기
# 처음 들어온 queue가 빌 때까지 진행
# 이후에 생기는 바이러스의 위치는 sub에 담고 sub return
def bfs(queue):
    sub = []
    while queue:
        t = queue.pop(0)

        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            si, sj = t[0] + di, t[1] + dj

            if lab[si][sj] == 0:
                lab[si][sj] = lab[t[0]][t[1]]  # 해당 바이러스 번호로 바꾸기
                sub.append([si, sj])

    return sub

# 2. input
n, k = map(int, input().split()) # 시험관 크기, 바이러스 번호
lab = [[-1]*(n+2)] + [[-1] + list(map(int, input().split())) 
+ [-1] for _ in range(n)] + [[-1]*(n+2)]
s, x, y = map(int, input().split()) # s초, (x, y)

# 2-2
# 바이러스 위치 찾아서 queue 만들기 > 바이러스 크기 순으로 정렬 필요
# virus는 위치가 key, 바이러스 번호가 value인 딕셔너리
queue = []
virus = {}
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if lab[i][j] != 0 :
            virus[(i, j)] = lab[i][j]

# 2-3 정렬
v = sorted(virus.values())
v = list(set(v))  # value의 중복값 제거
for i in v:
    for key, value in virus.items():
        if i == value:
            queue.append(key)

# 3
# bfs함수를 통해 return된 sub을 queue로 갱신, s초 만큼 돌린다.
for _ in range(s):
    queue = bfs(queue)

print(lab[x][y])