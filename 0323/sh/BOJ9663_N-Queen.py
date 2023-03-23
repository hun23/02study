n = int(input())


def solution(n):
    check_col = [False] * (n+1); check_d1 = [False] * (2*n); check_d2 = [False] * (2*n)
    def process(row):
        answer = 0
        if row == n+1:
            return 1
        for i in range(1,n+1):
            d1 = row+i-1; d2 = n + (row - i)
            if check_col[i] == False and check_d1[d1] == False and check_d2[d2] == False:
                check_col[i] = True; check_d1[d1] = True; check_d2[d2] = True
                answer += process(row+1)
                check_col[i] = False; check_d1[d1] = False; check_d2[d2] = False
        return answer
    answer = process(1)
    return answer

print(solution(n))