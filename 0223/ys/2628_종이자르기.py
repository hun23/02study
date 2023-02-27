'''


가장 큰 종이 조각의 넓이
0> 가로, 1>세로
'''
# 1
# 1) 가로선, 세로선이 어디에 생기는지 lst에 저장. 처음과 끝의 번호도 저장.
# 2) 선을 다 그은 후 > 바로 뒤의 번호를 빼서 rlt에 저장.(잘린 종이의 한 변의 길이)
# 3) 각 변을 모두 곱해서 사각형의 넓이 rlt에 저장
row, column = map(int, input().split()) # 가로, 세로
num = int(input())

# 1-2 잘린 선분
row_lst = [0, row]
column_lst = [0, column]

# 1-3 변의 길이
row_rlt = []
column_rlt = []
rlt = []

# 2
for _ in range(num):
    way, line = map(int, input().split())
    # 2-1
    # line의 조건. 가로선은 column을, 세로선은 row를 자른다.
    if way == 0:
        column_lst.append(line)
    elif way == 1:
        row_lst.append(line)

# 2-2
# 잘린 선 sort.
row_lst.sort()
column_lst.sort()

# 2-3
# lst에서 변의 길이 구하기
for i in range(len(row_lst) - 1):
    row_rlt.append(row_lst[i + 1] - row_lst[i])

for i in range(len(column_lst) - 1):
    column_rlt.append(column_lst[i + 1] - column_lst[i])

# 2-4
# 각 변 곱해서 잘린 사각형 넓이 rlt에 저장
for i in row_rlt:
    for j in column_rlt:
        rlt.append(i * j)

# 3. rlt에서 max 출력
print(max(rlt))

