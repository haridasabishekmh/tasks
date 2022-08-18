from itertools import product
import json

f = open ('/home/akitra/Documents/json/Data1.json', "r")
data = json.loads(f.read())
a=[]
No=len(data['data'])
for i in range(0,No):
    count=0
    if data['data'][i]['contact'] not in a:
        for j in range(0,No):
            if data['data'][i]['contact']==data['data'][j]['contact']:
                count=count+1        
            a.append(data['data'][i]['contact'])
        print("CUSTOMER NAME:",data['data'][i]['customername'],"-","NO:OF ORDERS:",count)
f.close()