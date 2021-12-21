class Cosmetics:
           def __init__(self,product,name,fruit):
               self.product=product
               self.name=name
               self.fruit=fruit
list=[]
n=int(input("enter the total number of products "))
for i in range(0,n):
    ptype=input("enter the product type ")
    name=input("enter the product name ")
    fruit=input("enter the fruit included in the product ")
    list.append(Cosmetics(ptype,name,fruit))
for obj in list:
     print(obj.product,obj.name,obj.fruit)
ft=input("enter the fruit to check")     
ft=Cosmetics(ptype,name,fruit)
print(bool(ft))
