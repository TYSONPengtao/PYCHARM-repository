a=eval(input("请输入一个年份："))
if a%400==0:
    print(a,"是闰年")
elif a%4==0 and a%100!=0:
    print(a, "也是闰年")
else:
    print(a,"是平年")