import sys
sys.stdin = open("specialsort_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int,input().split()))

    lst = []
    while len(lst) < 11:
        for i in range(N):
            if i == max(num):
                lst.append(i)
                del num[i]

            elif i == min(num):
                lst.append(i)
                del num[i]

        if len(lst) == 10:
            break

    print(lst)

    ########틀림