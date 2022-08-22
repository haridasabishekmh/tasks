from itertools import product
import json

f = open ('/home/akitra/Documents/json/Data1.json', "r")
data = json.loads(f.read())
No=len(data['data'])
for i in range(No):
        if len(data['data'][i]['contact'])!=10 and ".com" not in data['data'][i]['email']:
            print(data['data'][i]['customername'],"HAS INVALID CONTACT DETAILS")
for i in range(No):
        if ".com" not in data['data'][i]['email']:
            print(data['data'][i]['customername'],"HAS INVALID E-MAIL ADDRESS")


f.close()