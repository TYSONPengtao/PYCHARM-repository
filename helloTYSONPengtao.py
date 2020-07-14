import random
password=random.randint(0,10)
tries=3
while tries>0:
    my_answer = int(input("请输入你猜的数字："))
    tries-=1
    if my_answer==password:
        print("猜对了，剩余次数{}".format(tries))
    elif my_answer>password:
        print("猜大了，剩余次数{}".format(tries))
    elif my_answer<password:
        print("猜小了，剩余次数{}".format(tries))
    else:
        print("DATA error!!!")
else:
    print("游戏结束！！")