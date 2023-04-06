'''
n*n 크기인 배열 a, 배열 a의 값은 각 행에 있는 모든 수의 합 중 최솟값을 의미한다.
회전 연산 수행 (r, c, s)
가장 왼쪽 윗칸 (r-s, c-s)
회전 연산이 두 개 이상이면, 연산을 수행한 순서에 따라 최종 배열이 다르다.
=> 배열 a의 최솟값 출력
'''

# 1
# k 순열 생성
def perm(i, k):
    if i == k:
        t = p[:]
        k_key.append(t)

    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            perm(i + 1, k)
            p[i], p[j] = p[j], p[i]

# 2
# 배열의 최솟값 출력
def arr_min(arr):
    global rlt

    for i in range(n):
        ans = 0
        for j in range(m):
            ans += arr[i][j]
        rlt = min(ans, rlt)


# 3
# 회전연산
def turn(r, c, s, arr):

    # top(left -> right)
    for t in range(s, 0, -1):
        tmp = arr[r-t][c+t]  # top right save
        arr[r-t][c-t+1:c+t+1] = arr[r-t][c-t:c+t]

        # left(bottom -> top)
        for col in range(r-t, r+t):
            arr[col][c-t] = arr[col+1][c-t]

        # bottom(right -> left)
        arr[r+t][c-t:c+t] = arr[r+t][c-t+1:c+t+1]

        # right(top -> bottom)
        for col in range(r+t, r-t, -1):
            arr[col][c+t] = arr[col-1][c+t]
        arr[r-t+1][c+t] = tmp

    return arr


# 4 input
n, m, k = map(int, input().split())  # 크기, 회전 연산의 개수
arr_main = [list(map(int, input().split())) for _ in range(n)]  # original 배열

p = [x for x in range(k)]
k_key = []
k_value = [list(map(int, input().split())) for _ in range(k)]

perm(0, k) # k_value의 인덱스 순열 만들기

# 5 함수 시작
rlt = 999999999
for i in range(len(k_key)):
    arr = [x[:] for x in arr_main]  # deepcopy

    for j in range(k):
        r, c, s = k_value[k_key[i][j]][0] - 1, k_value[k_key[i][j]][1] - 1, k_value[k_key[i][j]][2]
        arr = turn(r, c, s, arr)

    arr_min(arr)

print(rlt)

