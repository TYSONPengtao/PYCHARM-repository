from random import randint
n=randint(10,100)
tries = 3
while tries>0:
    my_guss = int(input("请输入你猜的价格："))
    tries -= 1
    if my_guss>n:
        print("猜大了！！剩余次数为{}".format(tries))
    elif my_guss<n:
        print("猜小了！！剩余次数为{}".format(tries))
    elif my_guss==n:
        print("猜测正确！！剩余次数为{}".format(tries))
    else:
        print("data error")
else:
    print("游戏结束了！！")