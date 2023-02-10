import sys
sys.stdin = open("input.txt", "r")

N = int(input())              # input 될 숫자
rlt = []                      # 결과 값을 받을 list

for backnum in range(1, N+1):
    lst = [N, backnum]        # [list[0] - list[1]]을 하기 위한 설정
    while True:
        # 리스트 맨 끝에 새로이 올 숫자는 기존 맨 끝의 하나 앞 - 기존 맨 끝
        next = lst[-2] - lst[-1]
        if next >= 0:
            lst.append(next)    # 정수가 나오면 lst에 추가하고
        else:
            break               # 아니면 다시해
        if len(lst) > len(rlt):     # 최대 개수의 수를 구해야 하므로 rlt 값 재할당
            rlt = lst

print(len(rlt))
print(*rlt)
