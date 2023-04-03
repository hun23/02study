def solve(depth, before, cost):
    global A, B, answer, used
    if depth == 0:  # 모든 강의실을 돌았으면
        answer = cost + arr[before][0]  # 0번 강의실로 돌아오는 비용 추가
        return answer
    elif not used[A] and used[B]:   # A번 강의실보다 B번 강의실에 먼저 도착한 경우
        return float('inf')
    elif cost > answer:             # 비용이 이미 이전 최소값보다 큰 경우
        return float('inf')

    ret = float('inf')
    for i in range(1, N):           # 0번 강의실은 제외
        if not used[i]:             # 아직 방문하지 않았으면
            used[i] = True
            # 비용 추가한 뒤 재귀
            ret = min(ret, solve(depth - 1, i, cost + arr[before][i]))
            used[i] = False
    return ret


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    A, B = map(int, input().split())
    answer = float('inf')  # 최솟값 비교 & 저장 위해 inf 로 초기화
    used = [False] * N
    print(f"#{tc} {solve(N - 1, 0, 0)}")  # 0번 강의실에서 시작
