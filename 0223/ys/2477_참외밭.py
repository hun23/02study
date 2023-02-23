'''
1.
1) 밭은 6각형이다 => max가로, 세로를 구하고 -> 파여진(안으로 들어가는) 작은 사각형의 넓이를 빼면 된다.
2) max 가로, 세로는 무조건 붙어 있다. 그리고 작은 사각형의 변의 길이는 max에 인접하지 않은 두 수이다.
3) 작은 사각형의 두 변을 구하기 위해서는 max 가로, 세로의 idx가 필요 => idx - 3이 작은 사각형의 변의 인덱스가 된다.
'''

# 2
melon = int(input())
d_farm = [0] * 6  # 방향 lst
l_farm = [0] * 6  # 길이 lst

for i in range(6):
    d, l = map(int, input().split())
    d_farm[i] = d
    l_farm[i] = l

# 3-1
# max row, column + 각각의 idx 구하기
# max값 갱신 및 idx 갱신
maxrow = 0
maxcolumn = 0
idx1 = 0
idx2 = 0
for i in range(6):
    if (d_farm[i] == 1 or d_farm[i] == 2) and l_farm[i] > maxrow:
        maxrow = l_farm[i]
        idx1 = i
    elif (d_farm[i] == 3 or d_farm[i] == 4) and l_farm[i] > maxcolumn:
        maxcolumn = l_farm[i]
        idx2 = i

# 3-2
# 작은 사각형의 변의 idx
idx1 -= 3
idx2 -= 3

# 4 넓이 구하기
big = maxrow * maxcolumn  # 큰 사각형
small = l_farm[idx1] * l_farm[idx2]  # 작은 사각형

print(melon*(big - small))
