# import sys
# sys.stdin = open("sample_input.txt")

# 1
# core의 인덱스와 방향을 받아서
# 전선 길이 return, 놓을 수 없다면 0 return
def wire(idx, d, arr):
    sub = [i[:] for i in arr]  # deepcopy
    x = core[idx][0]
    y = core[idx][1]

    direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    cnt = 0
    for k in range(1, n):
        i, j = x + direct[d][0] * k, y + direct[d][1] * k
        if 0 <= i < n and 0 <= j < n and sub[i][j] == 0:
            sub[i][j] = 1
            cnt += 1
        elif 0 <= i < n and 0 <= j < n and sub[i][j] == 1:
            cnt = 0
            sub = arr  # 연결되지 않으면 초기 상태로 바꾸기
            break
    return cnt, sub

# 2
# 길이를 받고
# 다음 방향으로 넘어가는 함수
def next_core(idx, arr):
    global coreCnt
    global wireLength
    global maxCore
    global minWire
    global dx

    if idx == dx:  # 일단 마지막까지 돌았다면, 정답 확인이 가능하다..! 최종적인 결과들 return

        '''
        1)cntCnt가 현재까지의 max보다 큰 경우, core개수와 wirelenght 모두 갱신
        2)같은 경우.. wireLenght를 비교해서 더 작은 것으로 갱신
        '''
        if coreCnt > maxCore:
            maxCore = coreCnt
            minWire = wireLength
        elif coreCnt == maxCore:
            minWire = min(minWire, wireLength)

        return

    else:
        for d in range(4):
            # direction 한 방향을 정해서 그 길로 전선을 놓을 수있는지 확인!
            lst = wire(idx, d, arr)  # 함수 돌림, 그럼 cnt, sub가 나온다...
            cnt = lst[0]
            arr = lst[1]
            if cnt != 0:  # 0이 아니면 코어를 더하고, 0이면 코어를 더하지 않고 다음으로 넘어가기
                coreCnt += 1
                wireLength += cnt
                next_core(idx + 1, arr)  # 다음으로 넘어갈 수 있다면,
                # 넘어갈 수 없다면 원래 상태로 만들기

                coreCnt -= 1
                wireLength -= cnt
            else:
                next_core(idx + 1, arr)


# 3
T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    maxinos = [list(map(int, input().split())) for _ in range(n)]

    direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # 3-2. core 위치 찾기(가장자리 제외)
    core = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if maxinos[i][j] == 1:
                core.append([i, j])

    dx = len(core)  # 전체 core 개수
    coreCnt = 0     # core count
    wireLength = 0  # wire 길이
    maxCore = 0     # core의 max
    minWire = n ** 2  # wire의 min

    # 3-3. 함수 시작
    next_core(0, maxinos)
    print(f'#{tc} {minWire}')
