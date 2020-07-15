my_job=int(input("请输入你的分数："))
my_show=my_job/10
if 0<=my_show<6:
    print("D")
elif 6<=my_show<8:
    print("C")
elif 8<=my_show<=9:
     print("B")
elif 9<my_show<=10:
    print("A")
else:
    print("data error!!!")
