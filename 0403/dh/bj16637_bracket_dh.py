def calculate(is_bracket):
    global line
    
    # divide line to numbers & operators(ops)
    op_idx = 0
    numbers, ops = [], []
    for letter in line:
        if letter.isdigit():
            numbers.append(int(letter))
        else:
            ops.append((is_bracket[op_idx], letter))
            op_idx += 1
            
    # calculate untill one number remains
    while len(numbers) != 1:
        # check brackets
        to_next = False
        for i in range(len(ops)):
            if ops[i][0] == 1:  # if bracket
                calculated = 0
                if ops[i][1] == "*":
                    calculated = numbers[i] * numbers[i + 1]
                elif ops[i][1] == "+":
                    calculated = numbers[i] + numbers[i + 1]
                elif ops[i][1] == "-":
                    calculated = numbers[i] - numbers[i + 1]
                numbers[i] = calculated
                del numbers[i + 1]
                del ops[i]
                to_next = True
                break
        if to_next:
            continue
        calculated = 0
        if ops[0][1] == "*":
            calculated = numbers[0] * numbers[1]
        elif ops[0][1] == "+":
            calculated = numbers[0] + numbers[1]
        elif ops[0][1] == "-":
            calculated = numbers[0] - numbers[1]
        numbers[0] = calculated
        del numbers[1]
        del ops[0]
    return numbers[0]

def recursion(is_bracket, op_len, idx):
    global answer
    if op_len <= idx:
        # calculate
        c = calculate(is_bracket)
        if answer < c:
            answer = c
        return

    is_bracket[idx] = True  # put bracket on idx'th operator
    recursion(is_bracket, op_len, idx + 2)  # jump to next-next operator
    is_bracket[idx] = False  # reset
    recursion(is_bracket, op_len, idx + 1)  # jump to next operator
    return

# 1 <= N <= 19 
# ===> 0 <= len(operators) <= 9
# ===> number of cases < 2**9(=512)
N = int(input())  # 1 ~ 19 -> 
line = list(input())
is_bracket = [False] * (len(line)//2)
answer = -2147483648  # !!!!!!!!!!
recursion(is_bracket, len(is_bracket), 0)
print(answer)