N = int(input())
arr = list(map(int, input().split()))
mx, asc, des = 1, 1, 1  # asc: 증가하는, des: 감소하는
for i in range(N - 1):
    if arr[i] < arr[i + 1]:  # 증가하면
        asc += 1  # 증가횟수 추가
        des = 1  # 감소횟수 초기화
    elif arr[i] > arr[i + 1]:  # 마찬가지
        des += 1
        asc = 1
    else:  # 같으면 둘 다 증가
        asc += 1
        des += 1

    # 최대값 갱신
    if mx < asc:
        mx = asc
    if mx < des:
        mx = des
print(mx)
