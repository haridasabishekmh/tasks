import time
import datetime
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
today = datetime.now()
ts = time.time()
print("Time Stamp :",ts)
print("(dd/mm/yyyy)format :",today.strftime("%d/%m/%Y"))
print("(mm/dd/yyyy)format :",today.strftime("%m/%d/%Y"))
print("(mm/dd/yyyy hh:mm:ss:ms)format :",today.strftime("%m/%d/%Y %H:%M:%S:%f"))
print("(mm/yyyy)format :",today.strftime("%b %Y"))
print("Date Region :",today.astimezone().tzinfo)