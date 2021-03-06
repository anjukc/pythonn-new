import csv 
dict_value = [
{"name":"Anju","MFC":44,"DC":33,"DS":39,"ASC":33},
{"name":"Raji","MFC":49,"DC":35,"DS":35,"ASC":38},
{"name":"Arun","MFC":44,"DC":33,"DS":39,"ASC":33},
{"name":"Anjana","MFC":33,"DC":35,"DS":33,"ASC":36},
{"name":"Nisha","MFC":25,"DC":33,"DS":39,"ASC":33},
{"name":"Lemi","MFC":39,"DC":38,"DS":45,"ASC":38},
{"name":"Feba","MFC":49,"DC":43,"DS":44,"ASC":49},
{"name":"Paru","MFC":43,"DC":35,"DS":38,"ASC":36},
{"name":"Salu","MFC":26,"DC":36,"DS":47,"ASC":39},
{"name":"Sara","MFC":44,"DC":36,"DS":32,"ASC":45}
]

fields = ["name","MFC","DC","DS","ASC"]

with open('marklist','W') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    csvfile.close()

with open('marklist.csv','W') as csvfiles:
    readerobj = csv.DictReader(csvfiles)
    for row in readerobj:
         print(row['Name'],":",float(float(int(row['MFC'])+int(row['DC'])+int(row['DS'])+int(row['ASE']))/400)*100,"%")
         mfc=mfc+int(row['MFC'])
         dc=dc+int(row['DC'])
         ds=ds+int(row['DS'])
         ase=ase+int(row['ASE'])
print("average ")
print("MFC",mfc/10)
print("DC",dc/10)
print("DS",ds/10)
print("ASE",ase/10)
