
def connect(pcss, arr, idx, connected, wire):
    global dr
    global dc
    global max_connected
    global min_wire_len

    if idx == len(pcss):  # update if max
        if connected >= max_connected:
            if connected == max_connected:
                min_wire_len = min(wire, min_wire_len)
            else:
                max_connected = connected
                min_wire_len = wire
        return
    elif len(pcss) - idx + connected < max_connected:  # pruning
        return

    for d in range(4):
        leng = 0
        r, c = pcss[idx]
        while True:
            leng += 1
            nr, nc = r + dr[d] * leng, c + dc[d] * leng
            if not (N > nr >= 0 and N > nc >= 0):  # arrived to wall

                # connect wire
                for le in range(1, leng):
                    nr, nc = r + dr[d] * le, c + dc[d] * le
                    if N > nr >= 0 and N > nc >= 0:
                        arr[nr][nc] = 1

                # move to next one
                connect(pcss, arr, idx + 1, connected + 1, wire + leng - 1)

                # de-connect wire for next direction
                for le in range(1, leng):
                    nr, nc = r + dr[d] * le, c + dc[d] * le
                    if N > nr >= 0 and N > nc >= 0:
                        arr[nr][nc] = 0
                break

            elif arr[nr][nc]:  # arrived to other processor
                connect(pcss, arr, idx + 1, connected, wire)  # leave without connection
                break
    return


dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    processors = list()  # get processors coordinates
    for r in range(N):
        for c in range(N):
            if arr[r][c]:
                processors.append((r, c))
    max_connected = 0
    min_wire_len = 2147483647

    connect(processors, arr, 0, 0, 0)
    print(f"#{tc} {min_wire_len}")
