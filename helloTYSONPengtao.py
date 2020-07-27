a=input("请输入数字a:")
b=input("请输入数字b:")
c=input("请输入数字c:")
print("输入顺序为：",a,b,c)
if a<b:
    a,b=b,a
if a<c:
    print("顺序为：",c,a,b)
else:
    if c>b:
        print("顺序为：",a,c,b)
    else:
        print("顺序为：",a,b,c)