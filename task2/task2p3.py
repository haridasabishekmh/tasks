from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
selection=input("ENTER C FOR CURRENT DATE AND ENTER D FOR CUSTOM DATE")
if "C"==selection:
    Cthree_months = date.today() + relativedelta(months=+3)
    print(Cthree_months)
elif "D"==selection:
    str_d = input("ENTER THE STARTING DATE")
    date = datetime.strptime(str_d, "%Y/%m/%d").date()
    Dthree_monts = date + relativedelta(months=+3)
    print(Dthree_monts)
else:
    print("INVALID OPTION")

