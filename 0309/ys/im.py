'''
사과 바이러스 퇴치
과수원의 바이러스 숫자 n*n 배열
차르봄바 > 상하좌우로 바이러스 퇴치
p칸 만큼의 바이러스만 퇴치 가능
한발의 차르봄바로 최대한 바이러스 박멸하고 싶다.
최대 바이러스 퇴치 가능 수
'''

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):

    n, p = map(int, input().split())  # 과수원 배열, 위력p

    apple = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(n):
            cnt = apple[i][j]  # 초깃값 저장
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                for mul in range(1, p + 1):
                    ni, nj = i + di * mul, j + dj * mul
                    if 0 <= ni < n and 0 <= nj < n:
                        cnt += apple[ni][nj]

            ans = max(ans, cnt)

    print(f'#{tc} {ans}')


