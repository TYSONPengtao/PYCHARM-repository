print("<<<<<<<<猜数字游戏>>>>>>>>")
import random
my_screat=random.randint(0,10)
def guss_number():
    tries = 3
    while tries>0:
        password=input("你有3次机会，请输入你猜的数字：")
        my_answer=int(password)
        tries-=1
        if my_answer==my_screat:
            print("猜对了！！剩余次数为{}".format(tries))
            break
        elif my_answer<my_screat:
            print("猜小了！！剩余次数为{}".format(tries))
        elif my_answer>my_screat:
            print("猜大了！！剩余次数为{}".format(tries))
        else:
                print("data eroor!!!")
    else:
        print("游戏结束")
guss_number()
