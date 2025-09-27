try:
    year = int(input("请输入年份："))
    if year%4 ==0:
        if year % 400 == 0:
            print("是闰年")
        elif year % 100 != 0:
            print("是闰年")
        else:
            print("不是闰年")
    else:
        print("不是闰年")
except ValueError:
    print("输入错误")# 在此处编写代码
