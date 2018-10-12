TempStr = input("请输入带有符号的温度值：")
while TempStr[-1] not in ['N','n']:
   if TempStr[-1] in ['F','f']:
       C = (eval(TempStr[0:-1]) - 32) / 1.8
       print("华氏温度{}转换为摄氏度温度是：{}C".format(TempStr,C))
   elif TempStr[-1] in ['C','c']:
       F = eval(TempStr[0:-1])*1.8 + 32
       print("摄氏温度{}转换为华氏温度是：{}F".format(TempStr,F))
   else:
       print("输入格式错误")
   TempStr = input("请输入带有符号的温度值：")
