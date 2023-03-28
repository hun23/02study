def calculate(operators):
    global line
    
    # divide line to numbers & operators(ops)
    op_idx = 0
    numbers, ops = [], []
    for letter in line:
        if letter.isdigit():
            numbers.append(int(letter))
        else:
            ops.append((operators[op_idx], letter))
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

def recursion(operators, op_len, idx):
    global answer
    if op_len <= idx:
        # calculate
        c = calculate(operators)
        if answer < c:
            answer = c
        return

    operators[idx] = 1  # put bracket on idx'th operator
    recursion(operators, op_len, idx + 2)  # jump to next-next
    operators[idx] = 0  # reset
    recursion(operators, op_len, idx + 1)  # jump to next
    return

N = int(input())
line = list(input())
operators = [0] * (len(line)//2)
answer = 0
recursion(operators, len(operators), 0)
print(answer)