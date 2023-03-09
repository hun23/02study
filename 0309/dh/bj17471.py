from collections import deque


def bfs(case):
    global graph, populations
    q = deque()
    visited = [False] * (len(populations) + 1)
    ret = 0
    q.append(case[0])
    visited[case[0]] = True
    while q:
        cur = q.popleft()
        ret += populations[cur - 1]
        for nex in graph[cur]:
            if not visited[nex] and nex in case:
                visited[nex] = True
                q.append(nex)
    for c in case:
        if visited[c] is False:
            return 0
    return ret


def solve(c1, c2):
    global answer
    # if abs(sum(c1) - sum(c2)) < answer:
    #     return  # 가지치기
    # BFS
    sum1, sum2 = bfs(c1), bfs(c2)
    if sum1 and sum2:
        diff = abs(sum1 - sum2)
        if diff < answer:
            answer = diff
    return


N = int(input())
populations = list(map(int, input().split()))
graph = {key: [] for key in range(1, N + 1)}
for n in range(N):
    inp = list(map(int, input().split()))
    graph[n + 1] = inp[1:]
answer = 1000

# 부분집합
for i in range(1<<N):
    case1, case2 = [], []
    for j in range(N):
        if i & (1<<j):
            case1.append(j + 1)
        else:
            case2.append(j + 1)
    if len(case1) != 0 and len(case2) != 0:
        # print(f"i:{i} case1:{case1} / case2:{case2}")
        solve(case1, case2)
        case1.clear()
        case2.clear()
if answer == 1000:
    answer = -1
print(answer)
