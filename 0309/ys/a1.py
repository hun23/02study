'''
1번 사과를 먹으면 2번, 3, 번.... 먹기
좌측 상단으로 시작 위치 고정 / 뒤로 이동은 불가능, 오직 오른쪽으로만 회전 가능

회전 횟수를 최소화하여 순서대로 모든 사과를 먹으려면 최소 몇번의 회전이 필요한가.

!!기준!!
시작점에서 도착점이 right > 1번
시작점에서 도착점이 left > 2번

'''

import sys
sys.stdin = open("sample_input.txt")

# 1
# 회전 count하는 함수
# 시작점을 기준으로 도착점이 어느 사분면에 위치하느냐에 따라 회전수가 정해져 있다.
# 방향은 무조건 우하좌상 방향으로만 돌게 되고, 그 경우에 따른 회전수를 direction에 저장
# 방향(direct)는 cnt의 수에 따라 변화하므로 4 이상이 되면 갱신한다.
def circle(si, sj, ai, aj, direct):
    direction = [[1, 2, 3, 3], [3, 1, 2, 3], [3, 3, 1, 2], [2, 3, 3, 1]]
    cnt = 0
    if si < ai and sj < aj:
        cnt = direction[direct][0]
    elif si < ai and sj > aj:
        cnt = direction[direct][1]
    elif si > ai and sj > aj:
        cnt = direction[direct][2]
    elif si > ai and sj < aj:
        cnt = direction[direct][3]

    return cnt

# 2
# 사과의 위치 찾기
T = int(input())
for tc in range(1, T + 1):
    # 2-1 초기설정
    n = int(input())
    apple = [list(map(int, input().split())) for _ in range(n)]
    apple_idx = sum(apple, []) # 2차원 배열 > 1차원 리스트
    apple_dict = {0 : (0, 0)} # key가 사과 번호, value가 사과의 위치인 딕셔너리
    apple_lst = [0]  # 사과 번호

    # 2-2
    # 사과 위치 딕셔너리 만들기
    # 사과 번호 lst에 저장
    for i in range(n*n):
        if apple_idx[i] != 0:
            apple_dict[apple_idx[i]] = divmod(i, n)  # 딕셔너리로 사과 위치 저장
            apple_lst.append(apple_idx[i])
    apple_lst.sort()  # 오름차순으로 정렬

    # 2-3
    # 회전 수 찾기
    apple_cnt = []  # 회전cnt 모음
    direct = 0 # 방향은 0으로 시작
    for s in range(len(apple_lst) - 1):
        si, sj = apple_dict.get(apple_lst[s])  # 시작
        ai, aj = apple_dict.get(apple_lst[s + 1])  # 도착

        k = circle(si, sj, ai, aj, direct) # 회전수 함수
        apple_cnt.append(k)  # 회전 수 더하기

        direct += k  # direct에 cnt수 더하고
        if direct >= 4:  # 3 이상이면 갱신
            direct %= 4

    print(f'#{tc} {sum(apple_cnt)}')