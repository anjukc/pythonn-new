l1=[2,4,1,3,5,7,8,9]
l2=[2,4,5,7,8]
s=len(l1)==len(l2)
p=sum(l1)==sum(l2)
print("lenght are same:",s)
print("sum are equal:",p)
 M=[i for i in l1:i for i in l2]
print("common elements:",M)
