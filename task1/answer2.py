from itertools import product
import json
f = open ('/home/akitra/Documents/json/Data1.json', "r")
data = json.loads(f.read())
No=len(data['data'])
print("----------------------------------------------------------------------------------------------------------------------------------------")
for i in range(0,No):
    print("*","orderNo"," orderdate","\t","customername","\t","contact","\t","email","\t\t","taxpercentage","\t","netamount",)
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(data['data'][i]['orderNo'],"\t",data['data'][i]['orderdate'],"\t",data['data'][i]['customername'],"\t",data['data'][i]['contact'],"\t",data['data'][i]['email'],"\t\t",data['data'][i]['taxpercentage'],"\t",data['data'][i]['netamount'])
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    np=len(data['data'][i]['product'][0]['productid'])
    for j in range(0,np):
        print("Product ID","\t","Product Name","\t","Product Quantity","\t","Product Rate","\t","Product Price")
        print(data['data'][i]['product'][0]['productid'][j],"\t\t",data['data'][i]['product'][0]['name'][j],"\t\t",data['data'][i]['product'][0]['qty'][j],"\t\t\t",data['data'][i]['product'][0]['rate'][j],"\t\t",data['data'][i]['product'][0]['price'][j])
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        
        
f.close()