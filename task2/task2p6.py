import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta 
from dateutil.relativedelta import relativedelta

datest=input("Enter the starting date:")
date = datetime.strptime(datest, "%Y/%m/%d").date()
nofmnts=int(input("Enter no of months:"))
#datedup=date
print("EMI DATES")
for dateinc in range(0,nofmnts):
    emi_monts = date + relativedelta(months=+1)
    date=emi_monts 
    wkday=(emi_monts.strftime("%A"))
    if wkday == "Sunday":
        print(emi_monts+timedelta(1))
    elif wkday == "Saturday":
        print(emi_monts-timedelta(1))
    else:
        print(emi_monts)