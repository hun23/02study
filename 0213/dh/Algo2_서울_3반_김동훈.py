T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    r, c = map(int, input().split())
    point = 0
    for n in range(N):  # when duduji appears
        A, B, K = map(int, input().split())
        # get mangchi to duduji distance
        dis = abs(r - A) + abs(c - B)
        # compare K & distance
        if K >= dis:  # K >= distance
            point += 1  # get point
            r, c = A, B  # update r, c
        else:  # K < distance
            while K > 0:
                if c != B:  # move horizontally first
                    c += (1 if c < B else -1)
                elif r != A:  # move vertically when c == B
                    r += (1 if r < A else -1)
                K -= 1
    print(f"#{tc} {point}")
