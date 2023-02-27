
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list()
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    cost = 0   # 나무를 심는 총 비용
    cnt = 0    # 심어진 나무의 그루 수
    mx = 0     # 가장 비싼 나무의 가격
    line = 0   # 가장 비싼 나무가 심어진 열
    for i in range(N):
       for j in range(M):
            if j % 2 == 0:   # idx j % 2 == 0  -> idx[0]을 포함한 짝수열
                cost += arr[i][j]   # 금액에 그 칸의 비용을 추가
                cnt += 1    # 심은 나무의 그루 수 +1
            if j % 2 == 0 and arr[i][j] >= mx:  # 심을 칸에 해당되면서, 더 비쌀 때
                # input 값을 보니 같은 가격의 나무가 존재한다.
                mx = arr[i][j]  # 가장 비싼 나무의 가격을 재지정 해준다.
                line = j + 1    # j = idx number 이므로 열 표시를 위해서는 j+1

    print(f'#{tc} {cost} {cnt} {mx} {line}')