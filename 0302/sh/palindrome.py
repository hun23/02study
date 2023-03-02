import sys
sys.stdin = open("palindrome_input.txt", "r")


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # NxN 글자판, M 길이의 회문
    arr = [input() for _ in range(N)]  # NxN 글자판

    def is_palindrome():  # 찾았을 때 찾는 작업을 그만 두기 위해 함수에 넣어 return 해준다.
        for i in range(N):
            for j in range(N - M + 1):  # N개 중 M 길이의 회문을 판별하기 위한 시행은 N-M+1번
                # row
                if arr[i][j:j + M] == arr[i][j:j + M][::-1]:  # row 회문 확인
                    print(f'#{tc} {arr[i][j:j + M]}')
                    return  # 종료

                # col
                for k in range(M // 2):  # 양쪽에서 왔을 때 같으면 된다(가운데 문자는 don't need it)
                    if arr[j + k][i] != arr[j + M - k - 1][i]:  # 회문이 아니면 break
                        break
                else:   # 회문일 경우
                    print(f'#{tc} ', end='')
                    for l in range(M):
                        print(arr[j + l][i], end='')
                    print()
                    return  # 종료

    is_palindrome()