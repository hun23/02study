T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    inp = list(map(int, input().split()))
    jechul = [False] * N # 제출한 여부 리스트
    for i in inp: # i번학생이 제출했으면 i - 1인덱스를 변경
        jechul[i - 1] = True
    answer = [] # 답 출력용
    for i in range(N):
        if not jechul[i]: # 제출하지 않았으면
            answer.append(str(i + 1)) # 추가
    ans = " ".join(answer)
    print(f"#{tc} {ans}")