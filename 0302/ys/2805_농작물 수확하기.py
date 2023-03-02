T = int(input())

for tc in range(1, T + 1):
    # 1. 초기 설정
    n = int(input())
    farm = [list(input()) for _ in range(n)]
    harv = []  # 수확한 농작물 lst
    m = n // 2  # 중심 행

    # 2
    # k를 기준으로 farm슬라이싱, k는 0과 m사이의 값이다.
    k = 0
    for i in range(n):
        harv.append(farm[i][m - k:m + k + 1])  # 범위만큼 슬라이싱
        if i < m:
            k += 1
        else:
            k -= 1  # m을 찍었다면, -1 감소하면서 내려오기

    # 3
    # 문자 > 정수 변환
    # 수익 구하기
    harv = sum(harv, [])
    cost = 0
    for i in harv:
        cost += int(i)

    print(f'#{tc} {cost}')