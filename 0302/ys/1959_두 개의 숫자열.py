import sys
sys.stdin = open("input_숫자열.txt")

T = int(input())

for tc in range(1, T + 1):
    # 1. input
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    rlt = [] # 결과 담을 lst

    # 2
    # 3은 n < m 일때를 기준으로 하는 while문이다.
    # n > m 인 경우, (n,m) (a,b) 바꾸기
    if n > m:
        n, m = m, n
        a, b = b, a

    # 3
    j = 0
    while j < m - n + 1:
        cnt = 0
        for i in range(n): # a의 리스트를 하나씩 b와 곱해서 cnt에 합하고 rlt에 추가하기
            cnt += a[i] * b[i + j]

        rlt.append(cnt)
        j += 1  # b의 인덱스 이동

    print(f'#{tc} {max(rlt)}')