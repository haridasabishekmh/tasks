from itertools import product
import json

f = open ('/home/akitra/Documents/json/Data1.json', "r")
data = json.loads(f.read())
b=[]
a={"Name":[],"qt":[]}
N=len(data['data'])
for i in range(N):
    pn=len(data['data'][i]['product'][0]['productid'])
    for j in range(pn):
        a["Name"].append(data['data'][i]['product'][0]['name'][j])
        a["qt"].append(data['data'][i]['product'][0]['qty'][j])
ra=(len(a["Name"]))
for w in range(ra):           #code for count
    count=0
    if a["Name"][w] not in b:
        for z in range(ra):
            if a["Name"][w]==a["Name"][z]:
                count=count+int(a["qt"][z])       
        b.append(a["Name"][w])
        print("PRODUCT NAME:",a["Name"][w],"-","NO:OF ORDERS:",count)

f.close()