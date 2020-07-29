s,n=0,0
for i in range(1,11):
    score=eval(input("请输入你的成绩："))
    if score>=60:
        s=s+score
        n+=1
print("合格人数为：",n)
print("平均成绩为：",s/n)