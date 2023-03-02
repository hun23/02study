import sys
sys.stdin = open("hwcheck_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, do = map(int, input().split())
    K = list(map(int, input().split()))
    ans = []

    for i in range(1, N+1):  # 1번 부터 N번 까지니까
        if i not in K:       # 만약 i가 K에 없으면
            ans.append(i)    # 리스트에 추가

    print(f'#{tc}', end= " ")
    for i in ans:
        print((i), end = " ")
    print()