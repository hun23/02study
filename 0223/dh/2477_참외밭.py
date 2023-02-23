# 억지풀이
# k = int(input())
# inputs = []
# for _ in range(6):
#     a, b = map(int, input().split())
#     inputs.append((a, b))

# for i in range(6):
#     cut = []
#     temp_direction = [0, 0]
#     moves = {1: [], 2: [], 3: [], 4: []}
#     for j in range(6):
#         direction, value = inputs[j]
#         moves[direction].append(value)
#         if direction <= 2:
#             if direction == temp_direction[0]:
#                 cut.append(direction)
#             temp_direction[0] = direction
#         else:
#             if direction == temp_direction[1]:
#                 cut.append(direction)
#             temp_direction[1] = direction
#     if len(cut) == 2:
#         # print(cut)
#         area = sum(moves[1]) * sum(moves[3])
#         # print(area)
#         minus = moves[cut[0]][1] * moves[cut[1]][0]
#         print((area - minus) * k)
#         break
#     inputs.append(inputs.pop(0))


# 다른 풀이
k = int(input())
inputs = []  # 입력 (방향, 길이) 저장
box = {key: [] for key in range(1, 5)}  # 각 방향별로 분류
for _ in range(6):
    direction, length = map(int, input().split())
    box[direction].append(length)
    inputs.append((direction, length))

# 작은 사각형 변 구하기
# 어떤 변의 양 변의 방향이 같으면 해당 변은 작은 사각형의 변 중 하나이다
s = []
for i in range(6):
    try:  # i == 0인 경우 예외처리
        left_dir = inputs[i - 1][0]  # 입력 왼쪽의 방향 추출
    except:
        left_dir = inputs[-1][0]  # i==0일때, 왼쪽은 inputs의 마지막 변
    try:  # i == 5인 경우 예외처리
        right_dir = inputs[i + 1][0]  # 입력 오른쪽 방향 추출
    except:
        right_dir = inputs[0][0]  # i==5일때, 오른쪽은 inputs의 처음 변
    # 두 방향이 같으면
    if left_dir == right_dir:
        s.append(inputs[i][1])  # 작은변 리스트에 추가

# 큰 사각형 넓이 구하기
area = sum(box[1]) * sum(box[3])
# 작은 사각형 빼기
area = area - s[0] * s[1]
print(area * k)
