T = int(input())

for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = []

    done = False # for loop break를 위해 사용될 변수 변수 선언
    for x in range(1, N-1): # 양끝단을 제외한 중앙 값만 사용할 예정, 왜? 무조건 좌우가 1개 이상의 영역으로 둘러쌓인 값을 구할 것이기 때문
        for y in range(1, N-1): # 양끝단을 제외한 중앙 값만 사용할 예정, 왜? 무조건 상하가 1개 이상의 영역으로 둘러쌓인 값을 구할 것이기 때문
            maxV = arr[x][y] # max 값으로 설정, 만약 테두리 값 중 이보다 큰 값이 있으면 for loop break
            # 테두리 값을 미리 리스트에 삽입하여 사용
            cmp = [arr[x-1][y-1],arr[x-1][y],arr[x-1][y+1],arr[x][y-1],arr[x][y+1],arr[x+1][y-1],arr[x+1][y],arr[x+1][y+1]]
            for i in range(len(cmp)):
                # 만약 테두리 값보다 크다면 for loop 진행
                if arr[x][y] > cmp[i]:
                    continue
                # 만약 maxV보다 큰 테두리 값이 있다면 for loop 즉시 중단
                else:
                    done = True
                    break
            # for loop가 중단되지 않았을 경우에만, 즉 maxV 값보다 큰 테두리값이 없다면 이를 봉우리로 인정
            else:
                ans.append(maxV)

    # 봉우리가 1개이거나 없을 경우 -1 출력
    if len(ans) <= 1:
        print(f'#{tc} -1')
    # 그 외에는 가장 높은 봉우리 값에서 가장 낮은 봉우리 값의 차를 구하여 출력
    else:
        print(f'#{tc} {max(ans)-min(ans)}')