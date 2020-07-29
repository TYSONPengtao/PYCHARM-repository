x=eval(input("请输入你第一个数字："))
y=eval(input("请输入你第二个数字："))
if x<y:
    x,y=y,x
for i in range(x,x*y+1):
    if i%x==0 and i%y==0:
        print(x,"和",y,"的最小公倍数为",i)