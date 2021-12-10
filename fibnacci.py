n=int(input("enter the limit"))
a,b=0,1
sum=0
count=0
while(count<=n):
  print(sum,"\n")
  sum=a+b
  a=b
  b=sum
  count+=1
