'''

정육면체 1~6 까지의 숫자.

쌓을때, 붙는 면의 숫자가 같아야 한다.

옆면의 숫자들을 다 구해놓고, 돌릴 수 있으니까, 각각의 max를 더하기만 하면 된다.
=> 어떻게 쌓아 올리는 것이 중요..!

위에 올라오는 것만 제거.

'''

n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]

# 1
# bottom으로 top 찾는 함수
def direction(bot, i):
    top = dice[0][0]
    fin = dice[i].index(bot)  # bottom의 인덱스
    if fin == 0:
        top = dice[i][5]
    elif fin == 1:
        top = dice[i][3]
    elif fin == 2:
        top = dice[i][4]
    elif fin == 3:
        top = dice[i][1]
    elif fin == 4:
        top = dice[i][2]
    elif fin == 5:
        top = dice[i][0]
    return top

# 2
# 각 i열에서, top과 bottom을 제외하고 그 중 max값을 nums에 합하면서 넣는다.
# 한 i열의 인덱스를 j라고 할때, top과 bottom의 케이스는 6가지 이므로 빈칸 6개 만들기
nums = [0] * 6

# 3
for j in range(6):
    for i in range(n):
        if i == 0:  # 첫번째 i열에서 시작하는 bottom을 구하고, 그 이후에는 갱신되는 bottom값을 사용한다.
            bot = dice[i][j]
            rlt = [direction(bot, i), bot]
            new = [x for x in dice[i] if x not in rlt]  # top과 bottom을 제외한 리스트 + max구해서 nums의 해당 인덱스에 넣기
            nums[j] += max(new)
            bot = rlt[0]   # bottom값을 함수로 구한 top 값으로 갱신
        else:
            rlt = [direction(bot, i), bot]
            new = [x for x in dice[i] if x not in rlt]
            nums[j] += max(new)
            bot = rlt[0]

print(max(nums))



