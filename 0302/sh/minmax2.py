import sys
sys.stdin = open("minmax2_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))       # 숫자 리스트를 쭉 받아서

    mx = num[0]    # mx -> num의 0번째 인덱스가 제일 크다고 가정하고
    for i in range(1, N):
        if mx < num[i]:   # mx보다 i번째 num이 더 크다면
            mx = num[i]    # 새로운 mx로 할당

    mn = num[0]         # mn -> num의 0번째 인덱스가 제일 작다고 가정
    for j in range(1, N):
        if mn > num[j]:  # mn보다 더 작은 게 있으면
            mn = num[j]  # 니가 제일 작다고 할당

    print(f'#{tc} {mx-mn}')
