from collections import deque
import sys


def qs_empty(qs):
    for q in qs:
        if len(q) != 0:
            return False
    return True


M, N, H = map(int, input().split())
# 토마토 위치 입력
# 입력받으면서 익힐 토마토 개수 세기, 시작점 찾기
boxes = []
start_points = []
tomatoes_to_ripe = 0
for h in range(H):
    box = []
    for n in range(N):
        inp = list(map(int, sys.stdin.readline().rstrip().split()))
        box.append(inp)
        for m in range(M):
            if inp[m] == 0:  # 익힐 토마토 개수 카운트
                tomatoes_to_ripe += 1
            elif inp[m] == 1:  # 시작점(익은 토마토)
                start_points.append((h, n, m))
    boxes.append(box)

# BFS, 위 아래 왼쪽 오른쪽 앞 뒤
dm = [0, 0, -1, 1, 0, 0]
dn = [0, 0, 0, 0, 1, -1]
dh = [1, -1, 0, 0, 0, 0]
ripe_count = 0
mx_day = 0
if len(start_points) == 0:  # 죄다 0으로 시작하는 경우
    answer = -1
elif tomatoes_to_ripe == 0:  # 익힐 토마토가 없는 경우
    answer = 0
else:
    answer = 1
    
    
    
# start point deque에 다넣기
q = deque()
for sp in start_points:
    q.append(sp)
while q:
    point = q.popleft()
    days = boxes[point[0]][point[1]][point[2]]
    if days > mx_day:
        mx_day = days
    # 이동 가능 6방향 탐색
    for d in range(6):
        nh = point[0] + dh[d]
        nn = point[1] + dn[d]
        nm = point[2] + dm[d]
        if H > nh >= 0 and N > nn >= 0 and M > nm >= 0:
            if boxes[nh][nn][nm] == 0:
                boxes[nh][nn][nm] = days + 1
                ripe_count += 1
                q.append((nh, nn, nm))
if answer == -1 or tomatoes_to_ripe > ripe_count:
    print(-1)
elif answer == 0:
    print(0)
else:
    print(mx_day - 1)

# start point 하나씩 BFS -> 시간초과
# for sp in start_points:
#     q = deque()
#     q.append(sp)
#     while q:
#         point = q.popleft()
#         days = boxes[point[0]][point[1]][point[2]]
#         if days > mx_day:
#             mx_day = days
#         # 이동 가능 6방향 탐색
#         for d in range(6):
#             nh = point[0] + dh[d]
#             nn = point[1] + dn[d]
#             nm = point[2] + dm[d]
#             if H > nh >= 0 and N > nn >= 0 and M > nm >= 0:
#                 # try:
#                 if boxes[nh][nn][nm] != -1:
#                     if boxes[nh][nn][nm] == 0:
#                         boxes[nh][nn][nm] = days + 1
#                         ripe_count += 1
#                         q.append((nh, nn, nm))
#                     elif days + 1 < boxes[nh][nn][nm]:
#                         boxes[nh][nn][nm] = days + 1
#                         q.append((nh, nn, nm))
# except:
#     pass

# start point 여러개 동시에 BFS -> 왜틀렸지?
# print(start_points)
# qs = [deque([sp]) for sp in start_points]
# # print(qs)
# while not qs_empty(qs):
#     points = []
#     for q in qs:
#         if len(q) == 0:
#             points.append((-1, -1, -1))
#         else:
#             points.append(q.popleft())
#     # points = list(map(lambda x: x.popleft(), qs))
#     # days = list(map(lambda x: boxes[x[0]][x[1]][x[2]], points))
#     days = []
#     for p in points:
#         if p == (-1, -1, -1):
#             days.append(-1)
#         else:
#             days.append(boxes[p[0]][p[1]][p[2]])
#     if max(days) > mx_day:
#         mx_day = max(days)
#     # 이동 가능 6방향 탐색
#     for (i, point) in enumerate(points):
#         if point != (-1, -1, -1):
#             for d in range(6):
#                 nh = point[0] + dh[d]
#                 nn = point[1] + dn[d]
#                 nm = point[2] + dm[d]
#                 if H > nh >= 0 and N > nn >= 0 and M > nm >= 0:
#                     if boxes[nh][nn][nm] == 0:
#                         boxes[nh][nn][nm] = days[i] + 1
#                         ripe_count += 1
#                         qs[i].append((nh, nn, nm))
# #         print(f"qs: {qs}")
# #         for b in boxes:
# #             for bb in b:
# #                 print(bb)
# #         print()
# print(tomatoes_to_ripe)
# print(ripe_count)
