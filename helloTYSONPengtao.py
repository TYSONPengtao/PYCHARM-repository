n=2011
china=13.4
india=12.1
bingo=False
while bingo==False:
    if china>=india:
        china+=china*0.0048
        india+=india*0.012
        n=n+1
    else:
        print("印度在{}年超过中国".format(n))
        break
else:
    print("计算结束")


