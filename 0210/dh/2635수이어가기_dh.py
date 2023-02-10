first = int(input())
answer = []
mx = 0
if first == 1:  # edge case 주의!
    print(4)
    answer = [1, 1, 0, 1]
    print(*answer, sep=" ")
else:
    for second in range(1, first):  # first > 1인 경우
        arr = [first, second]  # 정답 저장 배열
        temp = [first, second]  # 값 계산 위한 임시 배열
        nex = temp[0] - temp[1]
        while nex >= 0:
            arr.append(nex)
            temp[0] = temp[1]
            temp[1] = nex
            nex = temp[0] - temp[1]
        if len(arr) > mx:  # 최대길이 갱신시
            mx = len(arr)
            answer = arr[:]  # 정답 저장
    print(mx)
    print(*answer, sep=" ")
