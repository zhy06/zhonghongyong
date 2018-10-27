k=5

tem=0
while True:
    x=eval(input("请输入0-9之间的整数"))
    tem +=1
    if x>k:
        print("遗憾，太大了")
    elif x<k:
        print("遗憾，太小了")
    else:
        print("预测{}次,你猜中了".format(tem))
        break
        
