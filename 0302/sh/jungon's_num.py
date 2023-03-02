import sys
sys.stdin = open("jungon_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    multi = []
    mul = 0
    ans = []
    for i in num:
        mul = num[i] * num[i+1]
        multi.append(mul)
        
    for j in multi:
        if multi[j] // 10 < multi[j] % 10:
            ans.append(j)

    print(f'#{tc} {max(ans)}')