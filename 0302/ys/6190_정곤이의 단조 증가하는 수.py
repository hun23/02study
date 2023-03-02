'''
단조증가 : 각 숫자의 자릿수가 단순하게 증가(계속 같거나 증가해야 한다.)
'''

# 1
# 단조증가하는지 확인하는 함수
# 단조증가 -> return k / 단조증가x -> return -1
def check(k):
    kstr = str(k) # k -> str으로 전환하여 생각
    if k < 10: # 10보다 작으면 x
        return -1
    else:
        ans = int(kstr[0])  # 크기가 같을때 계속 갱신, 갱신을 하지 않는다면 단조증가x
        for i in range(1, len(kstr)):
            if int(kstr[i]) >= ans:
                ans = int(kstr[i])
            else:
                return -1
        else:
            return k

# 2
T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    a = list(map(int, input().split()))
    rlt = [] # 단조증가인지 확인한 결과 append

    for i in range(n):
        for j in range(i + 1, n):
            k = a[i] * a[j]
            rlt.append(check(k))

    print(f'#{tc} {max(rlt)}')