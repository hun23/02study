T = int(input())

for test_case in range(1, T+1):

    # 입력 변수
    N, K, A, B = map(int, input().split()) # 하늘 크기, 촬영 영역, 초점
    sky = [list(map(str, input().split())) for _ in range(N)] # 하늘에 보이는 전체 값 저장

    # 선언 변수
    star = (sum(sky, [])).count('*') # 초기 화면으로 보이는 별 개수
    x = (K-1)//2 # (K는 항상 홀수) 초점을 기준으로 한 확대 화면의 좌우 범위

    ans = -1 # 초기 값
    while True:
        temp = []
        if A-x < 0 or B-x < 0 or A+x >= N or B+x >= N: # 만약 확대 화면이 하늘의 영역을 벗어나면
            break

        for i in range(A-x, A+x+1): # 상하 범위
            for j in range(B-x, B+x+1): # 좌우 범위
                temp.append(sky[i][j]) # 해당 범위에 들어오는 값 temp에 저장

        if temp.count('*') != star: # temp에 저장된 별의 개수가 초기 별의 개수와 다르다면
            break
        else:  # temp에 저장된 별의 개수가 초기 별의 개수와 같다면
            x -= 1 # 초점을 기준으로 상하좌우 범위를 1씩 줄임
            ans += 1 # 확대 횟수 +1
            continue # while loop 반복

    print(f'#{test_case} {ans}')