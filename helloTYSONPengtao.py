#一元二次方程求解
a=eval(input("请输入a:"))
b=eval(input("请输入b:"))
c=eval(input("请输入c："))
d=b**2-4*a*c
if d>=0:
    x1=(-b+d**0.5)/(2*a)
    x2=(-b-d**0.5)/(2*a)
else:
    print("input data error!!")