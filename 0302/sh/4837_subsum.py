import sys
sys.stdin = open("subsum_input.txt", "r")

T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


for tc in range(1, T + 1):               ### 비트 연산자를 통한 부분집합 전체 생성
    N, K = map(int, input().split())
    length = len(A)
    ans = 0

    for i in range(1 << length):
        cnt = 0                       # cnt = 원소의 개수
        sum_ = 0                      # sum_ = 원소의 합
        for j in range(length):
            if i & (1 << j):
                cnt += 1
                sum_ += A[j]          ### 비트연산자를 통한 부분집합 전체 생성 종료

        if cnt == N and sum_ == K:
            ans += 1
    print(f'#{tc} {ans}')