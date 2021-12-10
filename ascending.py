
import operator
d={3:5,1:3,4:2,5:1,2:4}
asc=(sorted(d.items(),key=operator.itemgetter(0)))
des=(sorted(d.items(),key=operator.itemgetter(0),reverse=True))
print("ascending order",asc)
print("descending order",des)
          
