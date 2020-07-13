print("<<<<<<<<彭涛>>>>>>>>")
password=input("请输入你猜的数字：")
my_anwser=int(password)
if my_anwser==8:
    print("good you win!!!")
elif my_anwser<8:
    print("猜小了！！！")
else:
    print("猜大了！！")
print("游戏结束！！")