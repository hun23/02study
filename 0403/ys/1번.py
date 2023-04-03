
# 10진수 -> 2진수
def change2(x):
    global rlt
    if x == 0:
        return '0' + rlt
    elif x == 1:
        return '1' + rlt

    else:
        if x % 2 == 0:  # 나머지가 0
            rlt = '0' + rlt
            change2(x // 2)
        elif x % 2 == 1:  # 나머지가 1
            rlt = '1' + rlt
            change2(x // 2)


T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    n16 = input()

    # 16진수 -> 10진수
    nums = int(n16, 16)
    print(nums)
    rlt = '1'
    change2(nums)  # 10진수 -> 2진수
    print(rlt)


    cnt = 0
    cnt_lst = []  # 연속된 1의 개수 넣는 lst -> 이 lst에서 최댓값 출력
    for i in range(len(rlt)):
        if rlt[i] == '1':
            cnt += 1
        else:
            cnt_lst.append(cnt)
            cnt = 0

    cnt_lst.append(cnt)

    print(f'#{tc} {max(cnt_lst)}')

