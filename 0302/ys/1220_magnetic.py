'''
파 > n극 / 빨 > s극
교착상태가 아니면 테이블 아래로 떨어진다.
교착상태 : ns가 붙음.
n극 : 1
s극 : 2
=> 교착상태의 개수 출력
=> 테이블로 떨어지는 자성체를 제외하고 나열했을때, ns가 바뀌는 횟수
=> 1로 시작해서 2로 끝나는 리스트에서 숫자가 몇번이나 바뀌는지 세야 한다.
'''

import sys
sys.stdin = open("input.txt")

'''
테이블로 떨어지는 자성체를 제외하고 나열했을 때, n/s가 바뀌는 횟수
=> 1,2로 이루어진 리스트에서 숫자가 몇번이나 바뀌는지 count
=> 2로 시작하거나 1로 끝나는 경우 count -1
'''

T = 10

for tc in range(1, T + 1):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    # 1
    # 열기준 순회
    total = 0
    for j in range(n):
        m = []
        for i in range(n):
            if table[i][j] != 0:
                m.append(table[i][j]) # j열 고정, 0이 아닌 원소 담기

        # 2
        # 교착상태 cnt
        # m의 길이가 1 이상이어야 count. 1인 경우 테이블 밑으로 떨어짐
        cnt = 0
        if len(m) > 1:
            for i in range(1, len(m)):
                if m[i] != m[i - 1]:  # 전과 다르면 cnt+1
                    cnt += 1

        if cnt == 1 and m[0] == 2 and m[-1] == 1 :  # cnt
            cnt = 0

        else:
            if m[0] == 2: # 2로 시작하면 -1 (table 밑으로 떨어진다)
                cnt -= 1

            elif m[-1] == 1: # 1로 끝나면 -1
                cnt -= 1

        total += (cnt // 2) + 1

    print(f'#{tc} {total}')