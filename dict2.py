import operator
imp_dict={4:5,1:2,3:2}
print("dictionary=",imp_dict)
sort_dict=dict(sorted(imp_dict.items())
key=(operator.itemgetter(0))
print("sorted dictionary by value="sort_dict)
