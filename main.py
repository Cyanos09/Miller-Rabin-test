#It is highly probable that it can be judged as a prime number or not, but it is not a reliable judgment.
import random
import math

def mrtest(n):
    x=0
    y=3
    i=0
    tmp=0
    flag=0

    if(n>2 and n%2==0):
        return False
    
    while y&1 == 0:
        p = pow(2,x)*y
        if(p == n-1 and x>=0 and y&1 == 1):
            flag = 1
            break
        x+=1
        y>>1

    r = random.randint(1,n-1)

    if(pow(r,y,n) == 1):
        return True
    
    while(i<x):
        tmp = pow(2,i) * y
        if(pow(r,tmp,n) == -1):
            return True
        i+=1

    return False

num = int(input("enter the number : "))
bl = mrtest(num)
if(bl==True):
    print("This number is likely to be prime.")
else:
    print("This number is not prime.")