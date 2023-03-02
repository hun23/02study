'''
0 : 빈용기
1~9 : 화학물질 종류에 따라

1) 화학물질이 담긴 용기 => 안에 0이 없다.
2) 용기들은 차원이 다르다 (가로*세로)
3) 2개의 화학물질이 담긴 용기들로 이루어진 사각형들 사이에는 빈 용기들이 있다. => 용기들이 떨어져 있다.

행렬들의 개수, 행렬들의 행과 열의 크기 출력/ 행*열 의 크기가 작은 순서대로 / 크기가 같으면 i가 작은 순서대로
'''

import sys
sys.stdin = open("input (1)_행렬찾기.txt")

# 1
# 가로 탐색 > j
def row(i, j):
    for k in range(j, n):  # i는 고정
        if box[i][k] != 0:
            continue
        else:
            return k - 1  # 0이 아닌 지점의 j값 return

# 2
# 세로 탐색 > i
def column(i, j):
    for k in range(i, n):  # j는 고정
        if box[k][j] != 0:
            continue
        else:
            return k - 1  # 0이 아닌 지점의 i값 return

# 3
# 용기가 발견된 부분 0으로 만들기
def whitepage(i, j, k, f):
    for n in range(i, k + 1):
        for m in range(j, f + 1):
            box[n][m] = 0


# 4
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    box = [list(map(int, input().split())) for _ in range(n)]
    memo = [] # 행 길이,열 길이 lst
    size = [] # 크기 lst

    i = 0
    while i < n:
        for j in range(n):
            if box[i][j] != 0:
                k = column(i, j) # 가로
                f = row(i, j) # 세로
                memo.append(k-i+1) # 행 길이
                memo.append(f-j+1) # 열 길이
                size.append((k-i+1)*(f-j+1)) # size 계산
                whitepage(i, j, k, f) # 빈페이지 만들기
                i = 0
                break
        else:
            i += 1

    # 5
    # bubble sort : size를 오름차순 정렬하면서, memo의 요소의 위치도 바꾼다.
    for j in range(len(size) - 1, 0, -1):
        for i in range(0, j):
            if size[i] > size[i+1]:
                memo[i*2], memo[i*2+1], memo[(i+1)*2], memo[(i+1)*2+1] = memo[(i+1)*2], memo[(i+1)*2+1], memo[i*2], memo[i*2+1] # 자리바꾸기
                size[i], size[i+1] = size[i+1], size[i]
            elif size[i] == size[i+1] and memo[i*2] > memo[(i+1)*2]:
                memo[i*2], memo[i*2+1], memo[(i+1)*2], memo[(i+1)*2+1] = memo[(i+1)*2], memo[(i+1)*2+1], memo[i*2], memo[i*2+1]

    print(f'#{tc} {len(memo)//2}', *memo)