def turn(N, arr, cnt):
    # cnt번 90도 돌리기
    ret = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ret[i][j] = arr[N-1 - j][i]
    if cnt == 0:
        return ret
    else:
        return turn(N, ret, cnt - 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    answer = [list() for _ in range(N)]
    for i in range(3):  # 각각 90, 180, 270회전
        temp = turn(N, arr, i)
        for n in range(N):
            answer[n].extend(temp[n] + [" "])  # 정답 출력 위해 가로로 저장
    print(f"#{tc}")
    for ans in answer:
        print("".join(ans))
