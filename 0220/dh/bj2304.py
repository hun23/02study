import sys


n = int(input())
pillars = []
# 기둥 (x좌표, 높이)을 pillars에 넣기
for _ in range(n):
    location, height = map(int, sys.stdin.readline().rstrip().split())
    pillars.append((location, height))
# 기둥 x좌표 기준으로 정렬
pillars.sort(key=lambda x: x[0])

# 데이터 전처리
before_len = n  # 삭제 이전의 기둥 개수
while True:  # 의미 없는 기둥 삭제(양 옆의 기둥보다 높이가 작은 기둥)
    to_delete = []  # 삭제할 기둥 인덱스 저장 리스트
    for i in range(1, len(pillars) - 1):
        y = pillars[i][1]
        # 양 옆의 기둥보다 높이가 작으면
        if pillars[i - 1][1] >= y and pillars[i + 1][1] >= y:
            to_delete.append(i)  # 삭제할 인덱스 리스트에 추가
    for d in to_delete[::-1]:
        # 삭제할 인덱스 리스트 돌며 삭제, 인덱스가 꼬이지 않기 위해 뒤에서부터 삭제
        del pillars[d]
    if before_len == len(pillars):
        # 삭제 이전의 기둥 개수와 삭제 이후의 개수가 같으면 더 지울것이 없으니 break
        break
    # 아니면 기둥 개수 업데이트
    before_len = len(pillars)

# 넓이 계산
_sum = 0
for i in range(len(pillars) - 1):
    cur_p = pillars[i]  # 현재 기둥
    next_p = pillars[i + 1]  # 다음 기둥
    if next_p[1] > cur_p[1]:  # 다음 기둥이 더 크면
        _sum += (next_p[0] - cur_p[0]) * cur_p[1]  # 현재 기둥 높이 * 기둥사이거리
    else:  # 다음 기둥이 더 작으면
        # 다음 기둥 높이 * 기둥 사이 거리
        _sum += (next_p[0] - cur_p[0]) * next_p[1]
# 가장 긴 기둥 따로 더하기
_sum += max(pillars, key=lambda x: x[1])[1]
print(_sum)
