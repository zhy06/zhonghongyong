import random
a=['羊1','羊2','汽车']
n=1000000
first,change=0,0
for i in range(n):
    x=random.choice(a)
    y=random.choice(a)
    if x==y:
        first +=1
    else:
        change +=1
print("坚持初心获得胜利的概率:{:.2f}%".format(first/n))
print("改变初心获得胜利的概率:{:.2f}%".format(change/n))
