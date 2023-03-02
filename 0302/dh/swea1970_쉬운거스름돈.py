T = int(input())
moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, T + 1):
    N = int(input())
    answer = [0] * 8
    for i, money in enumerate(moneys):  # 큰 단위부터
        while N >= money:  # 현재 액수가 더 크면
            N -= money  # 빼기
            answer[i] += 1
    print(f"#{tc}")
    print(*answer, sep=" ")
