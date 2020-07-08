def function():
    a=eval(input("请输入A的值："))
    b=eval(input("请输入B的值："))
    c=eval(input("请输入C的值："))
    d=b**2-4*a*c
    if d>=0:
        x1=(-b+d**0.5)/(2*a)
        x2=(-b-d**0.5)/(2*a)
        print("方程有实根,分别为x1={}和x2={}".format(x1,x2))
    else:
        print("方程无实根，请重新输入！！")
        function()
function()