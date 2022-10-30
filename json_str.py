import json

bill = '''{      "BillNumber":1245
                 ,"BillTotal":3000
                 ,"StoreLocation":"New York"
                 ,"BillDetails":[ { "Product":"Soda"
                                   ,"Quantity":10
                                   ,"UnitPrice":2
                                   ,"LineItemPrice": 20}
                                 ,{ "Product":"Chips"
                                   ,"Quantity":5.005
                                   ,"UnitPrice":3
                                   ,"LineItemPrice":15 }
                                 ,{ "Product":true
                                   ,"Quantity":4
                                   ,"UnitPrice":5
                                   ,"LineItemPrice":20 } ]
                 }'''

data = json.loads(bill)

# print(data)
# print(type(data))
# print(type(data["BillDetails"]))
# print(data["BillDetails"][1])

for items in data["BillDetails"]:
    #new_json = json.dumps(items)
    new_json1 = json.dumps(items,indent=2)
    new_json2 = json.dumps(items,indent=4)
    new_json3 = json.dumps(items,indent=8,sort_keys=True)


print (new_json1)
print (new_json2)
print (new_json3)


##################################################################

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
