a=float(input("请输入你的小数："))
b=float(a)
c=int(a)
e=b-c
if e>0:
    print(format(e,".2f"))
elif e==0:
    print(format(c,".2f"))
else:
    print("data errir!!!")
