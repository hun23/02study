from copy import deepcopy


def recursion(depth, arr, r, c):
    global answer, available
    if depth == 3:
        return
    nexts = get_nexts(r, c)
    for nex in nexts:  # 가능한 다음 좌표
        nr, nc = nex
        # 놓기
        if arr[nr][nc] == 1:  # 잡을 수 있는 돌로 표시
            arr[nr][nc] = 2
        original_ava = available[nr][nc]  # reset 위해
        available[nr][nc] = 0  # 잡았으니 삭제

        # 재귀
        recursion(depth + 1, arr, nr, nc)

        # 잡았던 돌 다시 놓기
        available[nr][nc] = original_ava
    return


def get_nexts(r, c):
    global dr, dc, available, N
    ret = []
    for d in range(4):  # 네방향중
        for n in range(1, N):  # 끝까지
            nr, nc = r + dr[d] * n, c + dc[d] * n  # 가려고 하는 좌표
            if not (N > nr >= 0 and N > nc >= 0):  # 일단 인덱스 범위 체크
                continue
            # r,c 와 nr,nc 사이에 available == 1 인 상태(생존한 알) 개수 체크
            cnt = 0
            if d < 2:  # 상하
                for drr in range(min(nr, r) + 1, max(nr, r)):
                    if available[drr][c] == 1:
                        cnt += 1
            else:  # 좌우
                for dcc in range(min(nc, c) + 1, max(nc, c)):
                    if available[r][dcc] == 1:
                        cnt += 1
            if cnt == 1:  # 하나만 있으면
                ret.append((nr, nc))
    return ret


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sr, sc, answer = 0, 0, 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                sr, sc = r, c
    available = deepcopy(arr)
    available[sr][sc] = 0
    arr[sr][sc] = 0
    recursion(0, arr, sr, sc)
    answer = sum(arr, []).count(2)
    print(f"#{tc} {answer}")