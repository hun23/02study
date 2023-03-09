'''
게리맨더링 > 자신의 당에게 유리하게 선거구 확정

n개의 구역으로 나누어져 있고, 두 개의 선거구로 나눠야 한다.
한 선거구에 포함되어 있는 구역은 모두 연결


print
두 선거구의 인구 차이의 최솟값 출력.
두 선거구로 나눌 수 없는 경우 -1 출력.
'''

# 1
# bfs함수
# 주어진 리스트가 연결되어 있는지 확인
def bfs(rlt):
    visited = [0] * (v + 1)
    s = rlt[0]  # 시작점은 rlt의 첫번째 점(시작점 상관 없이 이어진 것만 확인하면 된다)
    queue = []
    queue.append(s)
    visited[s] = 1  # 시작점에는 1찍기
    while queue:
        t = queue.pop(0)

        for i in rlt:
            if arr[t][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1 # 방문한 곳에 1찍기
    # 1-2
    # visited에 1이 rlt의 요소 개수 만큼 있다 > True, 없다 > False
    if visited.count(1) == len(rlt):
        return True
    else:
        return False

# 2
# 인구 수 구하는 함수
def population(rlt):
    ans = 0
    for i in rlt:
        ans += people[i]
    return ans

# 3
v = int(input()) # 구역 개수(노드 개수)

people = [0] + list(map(int, input().split())) # 인구수
arr = [[0] * (v + 1) for _ in range(v + 1)]  # 인접행렬

# 3-2
# 인접행렬 만들기
# 데이터를 한줄씩 받고, 인접 행렬을 표시한다.
for i in range(1, v):
    data = list(map(int, input().split()))
    for j in range(1, len(data)):
        n1, n2 = i, data[j]
        arr[n1][n2] = 1
        arr[n2][n1] = 1

# 4
# 선거구 부분집합 구하기
nodes = [x for x in range(1, v + 1)]
N = len(nodes)
lst = []  # 부분집합 리스트

for i in range(1 << N):
    temp = []
    for j in range(0, N):
        if i & (1 << j):
            temp.append(nodes[j])
    lst.append(temp)

# 5
# 구한 부분집합(선거구1) 다른 부분집합(선거구2)가 인접한지 확인
# 확인되면, 선거구의 인구수의 차이를 peo에 넣기
peo = [] # 선거구 인구수 차이
for district in lst:
    if district and district != nodes: # 리스트가 비어있지 않거나 전체가 아니라면, 부분집합의 반대 추출하기
        sub = [x for x in nodes if x not in district] # 선거구2
        if bfs(district) == True and bfs(sub) == True:
            peo.append(abs(population(district) - population(sub)))

# 6
# peo가 비어있다면 -1 출력
if peo:
    print(min(peo))
else:
    print(-1)




