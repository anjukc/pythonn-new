n=int(input("enter a number"))
s=0
a=0
while n>0:
    s=n%10
    a=a+s
    n=int(n/10)
print("sum of digits:",a)
