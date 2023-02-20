# https://www.acmicpc.net/problem/4949

while True:
    w = input()
    stack = []

    if w == '.':
        break
    
    for i in w:
        if i == '(' or i == '[':
            stack.append(i)
        
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
            
    if len(stack) == 0:
        print('yes')
    
    else:
        print('no')