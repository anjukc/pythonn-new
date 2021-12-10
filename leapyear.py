import datetime
year=int(input("enter the final year"))
tyear=datetime.datetime.now().year
for year in range(tyear,year+1):
 if year%4==0 or year%400==0:
print(years,"is a leap year")
