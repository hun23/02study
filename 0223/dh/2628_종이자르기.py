width, height = map(int, input().split())
cuts = int(input())
hor_cut = [0, height]
ver_cut = [0, width]
for cut in range(cuts):  # 입력 받고 자르기
    direction, idx = map(int, input().split())
    if direction == 0:
        hor_cut.append(idx)
    else:
        ver_cut.append(idx)

# 자르기 정렬
hor_cut.sort()
ver_cut.sort()
max_h = 0
max_v = 0

# 가로 / 세로 순회하면서 각 최대 길이 구하기
for i in range(len(hor_cut) - 1):
    diff = hor_cut[i + 1] - hor_cut[i]
    if diff > max_h:
        max_h = diff
for i in range(len(ver_cut) - 1):
    diff = ver_cut[i + 1] - ver_cut[i]
    if diff > max_v:
        max_v = diff
print(max_h * max_v)
