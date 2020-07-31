a=eval(input("请输入一个数："))
for i in range(2,a):
    if a%i==0:
        print(a,"不是素数")
        break
else:
    print(a,"是素数")