
x, y = map(int, input().split())  # 가로, 세로 길이
n = int(input())  # 상점 수

# 1
# 북>동>남>서 로 시계방향으로 이어진 한 줄
# road에서 방위에 따라 인덱스 찾는 함수
road = [0] * (2 * (x + y))
def index(a, b):
    if a == 1: # 북
        idx = b - 1
    elif a == 2: # 동
        idx = 2 * x + y - b - 1
    elif a == 3: # 남
        idx = 2 * x + 2 * y - b - 1
    elif a == 4: # 서
        idx = x + b - 1
    return idx

# 2
# 동근이의 위치가 마지막에 input되는 것 유의
# 먼저 road를 다 input 받아서 한줄의 리스트에 담는다.
road = [list(map(int, input().split())) for _ in range(n)]
road = sum(road, [])  # 한줄로 만들기

# 동근이의 위치 input
a1, b1 = map(int, input().split())
idx1 = index(a1, b1)

# 3
rlt = []
for i in range(0, 2 * n, 2):  # for문 돌때, i가 2씩 뛰어 넘도록
    # 3-1
    # index함수 활용해서 동근이의 위치와의 거리 구하기.
    idx2 = index(road[i], road[i + 1])
    route = abs(idx1 - idx2)

    # 3-2
    # route가 전체 거리의 1/2보다 작으면 route가 최단거리.
    # 아니면 (전체거리 - route)가 최단거리
    if route <= 2*(x+y) // 2:
       rlt.append(route)
    else:
        rlt.append(2*(x + y) - route)

print(sum(rlt))
