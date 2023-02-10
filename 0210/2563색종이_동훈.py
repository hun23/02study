N = int(input())
# 좌표 하나(1, 1)는 넓이 1을 의미하므로
# 중복 제거하는 set 사용
area = set()
for n in range(N):
    x, y = map(int, input().split())  # 색종이 좌표
    for r in range(10):  # 색종이 크기(10 * 10) 만큼
        for c in range(10):
            area.add((x + c, y + r))  # area 에 추가, 중복은 알아서 제거
print(len(area))  # area 의 길이 = 넓이
