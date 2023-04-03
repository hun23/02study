
# 순열 구하기
def promising(x):

    for i in range(0, x):
        if row[x] == row[i]:
            return False
    return True


def round(x):

    if x == n-1:
        if row.index(a) < row.index(b):
            t = [0] + row[:] + [0]  # 양 끝에 0 더해서 경로 구하기
            rlt.append(t)
        return

    else:
        for i in range(1, n):
            row[x] = i
            if promising(x):  # 유망하다면
                round(x+1)  # 재귀


# 2
T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    robot = [list(map(int, input().split())) for _ in range(n)]

    a, b = map(int, input().split())
    # 경로 정하기
    row = [0] * (n - 1)
    rlt = []
    round(0)


    # 에너지 구하기
    minANS = 9999999999
    for j in range(len(rlt)):
        ans = 0
        for i in range(len(rlt[j])-1):
            ans += robot[rlt[j][i]][rlt[j][i+1]]

        if ans < minANS:   # 최솟값 갱신
            minANS = ans


    print(f'#{tc} {minANS}')