xlen, ylen = map(int, input().split())
N = int(input())
shops = []
for n in range(N):
    a, b = map(int, input().split())
    shops.append((a, b))
dga, dgb = map(int, input().split())
dis = 0
for (a, b) in shops:
    temp = 0
    if dga == a:  # 같은 쪽
        temp += abs(b - dgb)
    elif dga + a == 3 or dga + a == 7:  # 다른쪽
        if dga <= 2:
            temp = min((dgb + b), (xlen - dgb + xlen - b))
            temp += ylen
        else:
            temp = min((dgb + b), (ylen - dgb + ylen - b))
            temp += xlen
    elif dga <= 2:  # 옆쪽
        if a == 3:
            temp += b if dga == 1 else (ylen - b)
            temp += dgb
        else:
            temp += b if dga == 1 else (ylen - b)
            temp += xlen - dgb
    elif dga <= 4:
        if a == 1:
            temp += b if dga == 3 else (xlen - b)
            temp += dgb
        else:
            temp += b if dga == 3 else (xlen - b)
            temp += ylen - dgb
    dis += temp
print(dis)
