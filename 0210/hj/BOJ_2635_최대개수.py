N = int(input())

_max = 0
_max_lst = []

for i in range(N+1):
    rlt = [N, i]
    j = 0
    while(True):
        num = rlt[j] - rlt[j+1]
        if num < 0:
            break
        rlt.append(num)
        if _max < len(rlt):
            _max = len(rlt)
            _max_lst = rlt[:]
        j += 1
print(_max)
for lst in _max_lst:
    print(lst, end=' ')
print()