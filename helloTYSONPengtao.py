def guss_job():
    tries=3
    while tries>0:
        a=int(input(
            "请输入你猜的数字a："
        ))
        b=int(input(
            "请输入你猜的数字b："
        ))
        if a==b:
            print(
            "猜测正确！"
                  )
            break
        else:
            tries-=1
            print(
            "剩余次数为{}"
            .format(tries))
    else:
        print(
            "次数用完！"
              )
guss_job()