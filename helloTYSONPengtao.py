from  time import sleep
n=eval(input("输入菱形总行数（奇数）："))
up=int((n+1)/2)
down=int((n-1)/2)
for i in range(1,up+1):
    print(" "*(up-i),end="")
    print("*"*(2*i-1))
sleep(0.5)
for i in range(1,down+1):
    print(" "*i,end="")
    print("*"*(n-2*i))
sleep(0.5)