N = int(input())
lst = list(map(int, input().split()))
cnt = []

# 나열된 숫자가 0개면 0
if N == 0:
    print(0)
# 나열된 숫자가 1개면 1
elif N == 1:
    print(1)
# 나열된 숫자가 2개 이상이면
else:
    # 연속해서 커지거나(cnt_up) 연속해서 작아지는(cnt_down) 수열의 개수 선언
    cnt_up = 1
    cnt_down = 1

    for i in range(N-1):

        # 연속해서 커지면
        if lst[i] < lst[i+1]:
            cnt_up += 1
            cnt.append(cnt_down)
            cnt_down = 1
        # 연속해서 작아지면
        elif lst[i] > lst[i+1]:
            cnt_down += 1
            cnt.append(cnt_up)
            cnt_up = 1
        # 같으면
        else:
            cnt_up += 1
            cnt_down += 1

    # 반복문 종료시 cnt_up, cnt_down 값 저장
    cnt.append(cnt_up)
    cnt.append(cnt_down)

    print(max(cnt))