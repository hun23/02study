'''
해야 할 v개의 작업. / 선행 관계가 있다.

일을 끝낼 수 있는 작업 순서 하나 제시.

dfs... ?

'''

import sys
sys.stdin = open("sample_input (1)_작업순서.txt")


# 1
# dfs 함수
# 선행관계(앞의 작업이 모두 처리 되어야 다음 작업에 넘어갈 수 있다.)
# dfs로 탐색하면서, 도착 지점에 연결된 부모노드를 파악하고
# => 그 부모 노드의 visited가 1이면 stack에 도착노드 push
# => visited가 1이 아니라면, 선행작업들이 수행되지 않았으므로 break, 스택에서 다른 노드 pop해서 탐색

def dfs(stack):
    while len(stack):  # 스택이 빌 때까지
        v = stack.pop()
        visited[v] = 1
        print(v, end=" ")

        # 열순회 고정
        for w in range(1, V + 1):
            if arr[v][w] == 1 and visited[w] == 0:  # 만족하는 w값 찾기
                for k in range(1, V + 1):  # w를 도착지점으로 하는 k의 visited가 1이어야 한다.
                    if arr[k][w] == 1 and visited[k] != 1: # 1이 아니면 break
                        break
                else:
                    stack.append(w)

# 2
T = 10
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    arr = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)

    # 2-1
    # arr[출발][도착]인 arr 만들기
    for i in range(E):
        n1, n2 = data[i * 2], data[i * 2 + 1]
        arr[n1][n2] = 1

    # 2-2
    # 시작점 찾기(stack에 시작할 수 있는 모든 점 넣기)
    # j열이 모두 0인것(부모 노드가 없는 것)
    stack =[]  # 스택에 시작점 넣기
    for j in range(1, V+1):
        for i in range(1, V+1):
            if arr[i][j] == 1:
                break
        else:
            stack.append(j)

    print(f'#{tc}', end=' ')
    dfs(stack)
    print()