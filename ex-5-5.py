def isPrime(n):
    for k in range(2,n):
        if n%k ==0:
            return False
    return True
while True:
    try:
        n = eval(input("Enter an Integer: "))
    except:
        print("Enter error! Please enter again: ")
        continue
    
    if type(n) is not int:
        print("Please enter an Integer: ")
        continue
