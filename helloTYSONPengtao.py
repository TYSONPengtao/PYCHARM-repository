#海伦公式
a=eval(input("请输入a边的值："))
b=eval(input("请输入b边的值："))
c=eval(input("请输入c边的值："))
if a>0 and b>0 and c>0:
    if (b+c>a) and (a+c>b) and (b+a>c):
        print(a,b,c,"构成三角形")
        p=(a+b+c)/2
        s=(p*(p-a)*p*(p-b)*p*(p-c))**0.05
        print("三角形的面积为：",s,end="")
    else:
        print("输入错误！！！")
else:
    print("三边必须是正数")