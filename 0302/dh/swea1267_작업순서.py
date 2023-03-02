for tc in range(1, 11):
    V, E = map(int, input().split())
    inp = list(map(int, input().split()))
    graph = {key: [] for key in range(1, V + 1)}  # 그래프 딕셔너리로 표현
    reverse_graph = {key: [] for key in range(1, V + 1)}  # 역방향 그래프
    visited = [False] * (V + 1)
    answer = []
    for i in range(0, len(inp), 2):  # 그래프 입력
        graph[inp[i]].append(inp[i + 1])
        reverse_graph[inp[i + 1]].append(inp[i])
    
    for k, v in reverse_graph.items():
        # 역방향 그래프의 원소가 비어있지 않으면
        # == 아직 먼저 할 일이 있으면
        if len(v) != 0:  
            continue  # 넘어간다
        # DFS
        stack = []
        stack.append(k)
        while stack:
            cur = stack.pop()
            nexts = graph[cur]
            if not visited[cur]:
                answer.append(str(cur))
                visited[cur] = True
                for nex in nexts:
                    reverse_graph[nex].remove(cur)  # 역방향에서 현재 그래프 제거
                    if len(reverse_graph[nex]) == 0:  # 역방향 원소가 비었으면
                        stack.append(nex)  # stack 에 추가
    print(f"#{tc} ", end="")
    print(" ".join(answer))
