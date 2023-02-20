'''
n개의 막대 기둥. => 지붕을 만든다.

1. 지붕은 수평, 수직부분으로 구성, 모두 연결
2. 지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
3. 지붕의 수직 부분은 ''
4. 지붕의 가장자리 => 땅.
5. 오목한 부분 x

가장 작은 창고 다각형의 면적

7
2 4
11 4
15 8
4 6
5 3
8 10
13 6

'''

# 1. 초기설정
n = int(input())  # 기둥 개수
# 1-1.
col = {}  # 기둥을 딕셔너로 받아서 => 정렬
for _ in range(n):
    l, h = map(int, input().split())
    col[l] = h
col1 = sorted(col.items())  # 정렬된 기둥 위치와 높이


# 1-2. 필요한 값들 변수 지정
left = col1[0][0]
right = col1[-1][0]
maxV = max(col.values())  # 가장 높은 기둥의 값
maximum = 0

for key, value in col.items():
    if value == maxV:
        maximum = key  # maximum = 가장 높은 기둥의 위치

max_idx = col1.index((maximum, maxV))  # 가장 높은 기둥의 리스트 안에서 인덱스 값

# 2 구하기
# 2-1. left ~ maximum까지 비교, 더 큰 기둥이 나오면 올라간다.
h = col1[0][1]
height = [h]     # 첫 h 넣고 시작, 지붕의 높이를 더할 리스트

if n >= 2 and col1[-1][1] == maxV:  # 마지막 기둥이 최댓값이라면, 넣고 시작.
    height.append(col1[-1][1])

j = 1  # 첫 h는 등록되었으므로, j는 1부터 비교하기
for i in range(left + 1, maximum + 1):
    if col1[j][0] < right and col1[j][0] == i:    # i를 for 문으로 돌리면서, 그 i값과 일치하는 값이 col1에 있을때(이때 co1[j][0]이 right보다는 작아야 함)
        if col1[j][1] >= h:                       # 현재의 h값과 비교해서, 크다면 h 올리기
            h = col1[j][1]
            height.append(h)
            j += 1
        else:                                     # 아니면 그냥 h 더하고, j의 인덱스 +1 하기
            height.append(h)
            j += 1
    elif col1[j][0] < right or i < right:         # 존재하지 않는다면, 기둥이 없는 곳이므로 현재의 h만 더하기
        height.append(h)

# 2-2. right~maximum 비교. 뒤에서부터 비교한다. 더 큰 기둥이 나오면 올라가기.
h = col1[-1][1]  # h값은 맨 뒤 기둥의 높이로 전환
j = n - 1  # j의 인덱스는 마지막으로
for i in range(right, maximum, -1):
    if col1[j][0] == i:
        if col1[j][1] >= h:
            h = col1[j][1]
            height.append(h)
            j -= 1
        else:
            height.append(h)
            j -= 1
    else:
        height.append(h)

print(sum(height))