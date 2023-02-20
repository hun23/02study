# https://www.acmicpc.net/problem/9012

import sys
T = int(sys.stdin.readline())


for test_case in range(T):
    PS = sys.stdin.readline()
    stack = []
    
    for i in PS:

        if i == '(':
            stack.append(i)
        elif i == ')':
                
            if stack:
                stack.pop()

            elif not stack:
                print('NO')
                break
        
        else:
            if len(stack) == 0:
                print('YES')
            elif len(stack) != 0:
                print('NO')