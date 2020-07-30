a=eval(input("请输入第一个数："))
b=eval(input("请输入第二个数："))
if b>a:
    a,b=b,a
for i in range(1,b+1): #i为最大公约数
    if a%i==0 and b%i==0:
        print(a,b,"最大公约数为：",i)