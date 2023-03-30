'''
n*n인 체스판 위에 퀸 n개를 서로 공격할 수 없게 놓는 문제
n이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램 작성
=> 퀸 자신을 기준으로 일직선상과 대각선 방향에 아무것도 x
백트래킹(backtracking)

1) 한 줄에 하나씩 들어온다.. -> 0번째 줄을 대상으로 경우의 수를 만들 수 있음

'''

'''
1.
cnt = n_queen이 성립하는 경우 count
row = 해당 인덱스의 열에서 퀸이 놓여지는 행의 인덱스 입력
'''
n = int(input())
cnt = 0
row = [0] * n

'''
2.
다음 인덱스로 넘어갈 수 있는지 확인한다.
false인 경우
1) 이전 인덱스와 같은 숫자.
2) 대각선 > 인덱스가 떨어진 만큼 차이 난다.
'''
def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True
'''
3.
1) 규칙들을 다 만족하는 x가 n인 경우 모두 통과했으므로 -> cnt+1
2) 아닌 경우, 확인하고 재귀로 돌린다. 
'''
def n_queens(x):
    global cnt
    if x == n:
        cnt += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):  # True이면, 가능하므로 다음 인덱스로 넘어가기 false이면 for문에서 다음 행의 인덱스로 넘어가기
                n_queens(x + 1)  # 다음 인덱스 확인~~~, 재귀가 진행되다가 x == n일때, return

'''
4. 인덱스 0부터 시작 ~~
'''
n_queens(0)
print(cnt)

