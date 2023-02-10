N = int(input())
numbers = list(map(int, input().split()))

## 증감이 없더라도 숫자는 최소 두개가 연속되므로
rlt1 = 2
rlt2 = 2
increase = 1
decrease = 1

# 리스트의 [num]번째와 [num+1]째 인덱스를 비교해서 [num+1]이 크면 increase에 +1
for num in range(0, N-1):
    if numbers[num] <= numbers[num+1]:
        increase += 1
        if increase > rlt1:    # 증가 수 > 초기값이면 결과값 재지정
            rlt1 = increase
        else:          # 아니면 rlt1 = 그냥 2
            rlt1
    else:
        increase = 1
# 리스트의 [i]번째와 [i+1]째 인덱스를 비교해서 [i+1]이 작으면 decrease에 +1
for i in range(0, N-1):
    if numbers[i] >= numbers[i+1]:
        decrease += 1
        if decrease > rlt2:    # 감소 수 > 초기값이면 결과값 재지정
            rlt2 = decrease
        else:
            rlt2            # 아니면 rlt2는 그냥 2
    else:
        decrease = 1



def result(rlt1, rlt2):
    if rlt1 > rlt2:
        return rlt1
    else:
        return rlt2


print(f'{result(rlt1, rlt2)}')
