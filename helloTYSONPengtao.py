from random import randint
n=randint(10,100)
print("请输入你猜的价格(10~100)")
bingo=False
while bingo==False:
    my_guss = eval(input("请输入你猜的价格："))
    if my_guss<n:
        print("猜小了！！")
    elif my_guss>n:
        print("猜大了！！")
    else:
        print("猜测正确！！价格是{}".format(my_guss))
        bingo = True
else:
    print("游戏结束！！")