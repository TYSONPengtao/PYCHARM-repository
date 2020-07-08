pi=3.14
def muliti_circle():
    r=eval(input("请输入圆的半径："))
    circleS=pi*r*r
    circleC=2*pi*r
    print("当圆的半径为{}时，圆的面积为{}，周长为{}".format(r,circleS,circleC))
    muliti_circle()
muliti_circle