# _*_ coding: UTF-8 _*_
import random

changes = ["", "石头", "剪子", "布"]
integral = 0


def show_changes():
    message = "\n"
    for index, value in enumerate(changes):
        if index == 0:
            continue
        message += "{0}. {1}".format(index, value)
        if index != len(changes) - 1:
            message += "  "
    return message


def compute_result(_me, _ra):
    global integral
    result = "错误"
    result = "平局" if _me == _ra else result
    result = "胜利" if _me == "1" and _ra == "2" or \
                     _me == "2" and _ra == "3" or \
                     _me == "3" and _ra == "1" else result
    result = "失败" if _me == "1" and _ra == "3" or \
                     _me == "2" and _ra == "1" or \
                     _me == "3" and _ra == "2" else result

    if result == "胜利":
        integral += 1
    if result == "失败":
        integral -= 1

    return result


def run_game():
    while 1:
        print show_changes()
        _me = str(raw_input("请出拳：").strip())
        _ra = str(random.randint(1, len(changes) - 1))
        res = compute_result(_me, _ra)

        try:
            changes[int(_me)]
        except:
            print "出拳错误！"
            continue

        print "你出<{0}> 对方出<{1}> 本次对战<{2}> 当前积分<{3}>".format(
            changes[int(_me)],
            changes[int(_ra)],
            res,
            integral
        )

        tp = raw_input("\n请选择是否退出（yes/no）: ").strip()
        if tp == "no":
            continue
        elif tp == "yes":
            print "已退出 ！"
        else:
            print "输入错误，已退出游戏！"
        break


print "游戏开始"
while 1:
    print
    print "*********************"
    print "1. 开始新游戏"
    print "2. 载入游戏"
    print "3. 退出"
    print "*********************"

    change = raw_input("请选择：").strip()
    print
    if change == "1":
        print "正在载入新游戏 ..."
        integral = 0
        run_game()
        print "您当前的得分是：{0}".format(integral)
    elif change == "2":
        print "正在载入 ..."
        run_game()
        print "您当前的得分是：{0}".format(integral)
    elif change == "3":
        break
    else:
        print "输入错误 ! 请重新输入 !"

print "游戏结束"