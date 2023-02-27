
T = int(input())
for tc in range(1, T+1):
    N, K, A, B = map(int, input().split())
    arr = list()
    for _ in range(N):
        arr.append(list(map(str, input().split())))

        stack1 = []
        zoom = -1
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] == '*':
                    stack1.append(arr[i][j])

        # stack2 = []
        # arr2 = arr[1:-1]
        # arr2 = arr2[0][1:]
    print(f'#{tc} {zoom}')
        # for i in range(N):
        #     for j in range(N):
        #         for _ in range(K):
        #             arr2.append(arr[1:-1])
        #             if arr2[i][j] == '*':
        #                 stack2.append(arr2[i][j])

        # if len(stack1) == len


        # zoom = 0
        # while True:
        #     for i in range(N):
        #         for j in range(N):
        #             if '*'