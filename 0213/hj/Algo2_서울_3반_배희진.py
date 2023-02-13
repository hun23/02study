T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    r, c = map(int, input().split())

    cnt = 0
    for _ in range(N):
        a, b, k = map(int, input().split())
        if abs(r-a)+abs(c-b) <= k: # 두더지가 나와있는 시간보다 빨리 이동 가능하면
            cnt += 1
            r = a
            c = b
        else: # 두더지가 나와있는 시간보다 빨리 이동이 불가능하면
            for _ in range(abs(r-a)+abs(c-b)):
                if r-a < 0:
                    r += 1
                elif r-a > 0:
                    r -= 1
                elif r-a == 0:
                    r = a
                k -= 1
                if k == 0:
                    break
                else:
                    if c-b < 0:
                        c += 1
                    elif c-b > 0:
                        c -= 1
                    elif c-b == 0:
                        c = b
                    k -= 1
                    if k == 0:
                        break

    print(f'#{test_case} {cnt}')