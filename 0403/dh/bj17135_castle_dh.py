from collections import deque
from copy import deepcopy

def find_target(N, archer):
    global visited, arr
    q = deque([(N, archer)])
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M): continue;
            if visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                if visited[nr][nc] <= D:  # if cell is in range D
                    if arr[nr][nc] == 1:  # and enemy is in the cell
                        return (nr, nc)  # then return to append to kill list
                    q.append((nr, nc))  # else continue BFS
    return None

dr = [0, -1, 0, -1]
dc = [-1, 0, 1, 0]

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
original = deepcopy(arr)
original_N = N
answer = 0

# get archer point
for i in range(M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            # reset variables
            arr = deepcopy(original)
            N = original_N
            temp_answer = 0
            # repeat untill arr is empty
            while N > 0:
                kill_list = set()  # coordinates of enemies to kill
                archers = [i, j, k]  # list of archer coordinates

                # fill kill list
                for archer in archers:
                    visited = [[0] * M for _ in range(N + 1)]
                    target = find_target(N, archer)  # BFS
                    if target is not None:
                        kill_list.add(target)
                
                # kill == make arr to 0
                for kill in kill_list:
                    arr[kill[0]][kill[1]] = 0
                    temp_answer += 1
                # print(f"ijk: {i} {j} {k}")
                # print(f"temp: {temp_answer}")
                # for a in arr:
                #     print(a)
                
                # cut arr
                arr = arr[:N-1]
                N -= 1
            if answer < temp_answer:
                answer = temp_answer
print(answer)