from datetime import datetime
from dateutil import relativedelta

str_d1 = input("ENTER THE STARTING DATE")
str_d2 = input("ENTER THE ENDING DATE")

d1 = datetime.strptime(str_d1, "%Y/%m/%d")
d2 = datetime.strptime(str_d2, "%Y/%m/%d")

delta=relativedelta.relativedelta(d2,d1)

print(f'Difference is',delta.years,"years",delta.months,"months",delta.days,"days")