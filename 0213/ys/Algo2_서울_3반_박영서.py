T = int(input())

for tc in range(1, T + 1):
    arr = [[0] * 10 for _ in range(10)]  # 게임판 10*10
    n = int(input())
    r, c = map(int, input().split())  # 망치 시작 위치
    cnt = 0  # 두더지를 때리는 횟수
    for _ in range(n):
        a, b, k = map(int, input().split())  # 두더지 좌표 a, b, k(머리 내미는 시간)

        # 대소비교
        if r < a:
            r, a = a, r

        if c < b :
            c, b = b, c

        # for문
        h = 1  # 시작!
        for i in range(r, a, -1):  # 가로 부터 시작
            for j in range(c, b, -1):
                h += 1
                r = i   # r, c의 값을 그 때의 i, j값으로 바꾼다
                c = j
                if h == k:   # 이동 횟수가 k랑 같아지게 된다면, 종료. r과 c는 그 자리에서 고정.
                    break

        if h < k:   # for문을 다 돌렸을때, h의 값이 k보다 작으면 cnt에 +1
            cnt += 1


    print(f'#{tc} {cnt}')










