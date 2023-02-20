import sys


def get_otherside(dice, downside_value):
    """
    downside_value(아랫면에 적힌 숫자)를 입력받아서
    마주보는 변의 값을 리턴
    """
    idx = dice.index(downside_value)
    if idx == 0:
        return dice[5]
    elif idx == 5:
        return dice[0]
    elif idx == 1:
        return dice[3]
    elif idx == 3:
        return dice[1]
    elif idx == 2:
        return dice[4]
    elif idx == 4:
        return dice[2]


def get_max_side(dice, downside_value):
    """
    downside_value(아랫면에 적힌 숫자)를 입력받아서
    옆면 중 최대값을 리턴
    """
    idx = dice.index(downside_value)
    sides = []
    if idx == 0 or idx == 5:
        sides += dice[1:5]
    elif idx == 1 or idx == 3:
        sides += [dice[0], dice[2], dice[4], dice[5]]
    elif idx == 2 or idx == 4:
        sides += dice[:2] + [dice[3], dice[5]]
    return max(sides)


# 디버깅 위해 주사위 프린트하기
def print_dice(down_value, dice):
    up_value = get_otherside(dice, down_value)
    print(f" {down_value} ")
    for value in dice:
        if value != up_value and value != down_value:
            print(f"{value}", end="")
    print()
    print(f" {up_value} ")


n = int(input())
# 주사위 입력
dices = []
for _ in range(n):
    dice = list(map(int, sys.stdin.readline().rstrip().split()))
    dices.append(dice)

# 계산
_sum = 0
for down_side in dices[0]:  # 첫번째(가장 아래) 주사위 각 면을 아랫면으로
    temp_sum = 0  # 이번 경우의 수 합
    for i in range(n):
        # print_dice(down_side, dices[i])
        # 아랫면이 down_side일때 옆면 중 최대값을 temp_sum에 더하기
        temp_sum += get_max_side(dices[i], down_side)
        # 다음 주사위의 아랫면 숫자 구하기
        down_side = get_otherside(dices[i], down_side)
    _sum = max(_sum, temp_sum)  # 이전 합과 이번 합을 비교 후 업데이트
print(_sum)
