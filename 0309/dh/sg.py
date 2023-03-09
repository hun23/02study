from copy import deepcopy


def solve2(before, after):
    global arr, positions
    br, bc = before
    ar, ac = after
    diff_r, diff_c = ar - br, ac - bc
    position = positions[((diff_r > 0), (diff_c > 0))]
    if position == 1 or position == 4:
        # 90
        transpose()
        lr_reverse()
        return 3
    elif position == 2:
        # 270
        lr_reverse()
        transpose()
        return 1
    elif position == 3:
        # 180
        lr_reverse()
        ud_reverse()
        return 2
    return 0


def transpose():
    global arr
    ret = [[0] * len(arr) for _ in range(len(arr))]
    for r in range(len(arr)):
        for c in range(len(arr)):
            ret[r][c] = arr[c][r]
    arr = deepcopy(ret)
    return


def lr_reverse():
    global arr
    ret = [[0] * len(arr) for _ in range(len(arr))]
    for r in range(len(arr)):
        for c in range(len(arr)):
            ret[r][c] = arr[r][len(arr) - c - 1]
    arr = deepcopy(ret)
    return


def ud_reverse():
    global arr
    ret = [[0] * len(arr) for _ in range(len(arr))]
    for r in range(len(arr)):
        for c in range(len(arr)):
            ret[r][c] = arr[len(arr) - r - 1][c]
    arr = deepcopy(ret)
    return


# up - left - down - right
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

positions = {(False, True): 1, (True, True): 2,
            (True, False): 3, (False, False): 4}

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # solve2
    answer = 0
    before, saga = (0, 0), (0, 0)
    saga_idx = 1
    while True:
        found = False
        for r in range(N):
            for c in range(N):
                if arr[r][c] == saga_idx:
                    saga_idx += 1
                    saga = (r, c)
                    found = True
                    break
            if found:
                break
        if not found:
            break
        answer += solve2(before, saga)
        found = False
        for r in range(N):
            for c in range(N):
                if arr[r][c] == saga_idx - 1:
                    before = (r, c)
                    found = True
                    break
            if found:
                break
    print(f"#{tc} {answer}")