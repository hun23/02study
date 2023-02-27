T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split()) # 행, 열
    arr = [list(map(int, input().split())) for _ in range(N)]

    sum = 0 # 전체 나무 가격의 '합'을 저장할 리스트
    cmp = [] # 전체 나무 가격의 '값'을 저장할 리스트, 이후 가장 비싼 나무를 탐색할 때 사용
    for j in range(0, M, 2):
        for i in range(N):
            sum += arr[i][j]
            cmp += [arr[i][j]]

    # cmp 리스트에서 max값을 찾고, 해당 값을 arr에서 찾아서 열 값을 출력
    loc = 0 # 가장 비싼 나무의 위치 초기 선언
    for j in range(0, M, 2): # 한 줄씩 띄어 나무 심기
        for i in range(N):
            if arr[i][j] == max(cmp): # 가장 비싼 나무의 값을 찾는다면
                loc = j+1 # 인덱스와 실제 열값의 차이가 1이기 때문에 +1
                # 가장 비싼 나무를 찾은 후에 break를 쓰지 않은 이유?
                # 동일한 가격의 나무가 뒤쪽 열에 위치한다면 해당 열로 갱신해주기 위해

    if M % 2 == 0: # 정원의 열이 짝수일 때 나무 개수
        tree = N * (M//2)
    else: # 정원의 열이 홀수일 때 나무 개수
        tree = N * (M//2+1)

    # 나무를 심는 총 비용, 심은 나무의 수, 가장 비싼 나무 가격, 가장 비싼 나무의 위치(열)
    print(f'#{test_case} {sum} {tree} {max(cmp)} {loc}')