import math
s=0
n=eval(input("输入:"))  #例12345
a=n
for i in range(1,6):   
    b=a%10  #获得最后一位数
    c=a//10 #去掉最后一位数
    a=c
    s=s+b*pow(10,5-i)
if s==n:
    print("是回文数")
else:
    print("不是回文数")
