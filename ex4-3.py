m,n=eval(input("请输入两个整数，中间以逗号隔开"))
if m<n:
    x,y=m,n
else:
    x,y=n,m
r=m%n
while r!=0:
    m,n=n,r
    r=m%n
print("{}和{}的最大公约数:{};最小公倍数:{:.0f}".format(x,y,n,x*y/n))

