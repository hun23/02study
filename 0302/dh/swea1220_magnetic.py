# 세로로 mp 돌면서
# 극의 종류가 하나면 패스
# 아니면 계산
# 2는 무시하다가 1이 있는데 2가 더 있으면 추가
for tc in range(1, 11):
    N = int(input())
    # mp 입력
    mp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        inp = list(map(int, input().split()))
        for j in range(N):
            mp[i][j] = inp[j]
    # 한 col씩 판단
    count = 0
    for col in range(N):
        found_n = False
        for row in range(N):
            if not found_n:
                if mp[row][col] == 1:
                    found_n = True
            else:
                if mp[row][col] == 2:  # s극을 찾으면
                    count += 1
                    found_n = False
    print(f"#{tc} {count}")