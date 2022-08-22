from itertools import product
import json

f = open ('/home/akitra/Documents/json/Data1.json', "r")
data = json.loads(f.read())
a=[]
No=len(data['data'])
for i in range(0,No):
    Sum=0
    if data['data'][i]['taxpercentage'] not in a:
        for j in range(0,No):
            if data['data'][i]['taxpercentage']==data['data'][j]['taxpercentage']:
                Sum=Sum+int(data['data'][j]['taxamount'])
            a.append(data['data'][i]['taxpercentage'])
       
        print("TAX PERCENTAGE:",data['data'][i]['taxpercentage'],"%","-","TOTAL AMOUNT:",Sum)
    
f.close()