from datetime import datetime
from dateutil import relativedelta

str_d1 = input("ENTER THE STARTING DATE")
d1 = datetime.strptime(str_d1, "%d/%m/%Y")
month=int(d1.month)
year=int(d1.year)
print(year)
if month <= 4:
    print("Fiscal year of",year-1,"-",year)
else:
    print("Fiscal year",year,"-",year+1)