import csv
import json

prod_master_data = []
total_bill = 0.0

## importing CSV
with open('products.csv','r') as f1:
    csv_data = csv.reader(f1)
    next(csv_data)
    for data in csv_data:
        prod_master_data.append(data)

## importing Json
f2 = open('20221104084722.json', 'r')
bill = json.load(f2)

## total calculation
for line_item in bill["BillDetails"]:
    for mstr_data in prod_master_data:
        if line_item == mstr_data[0]:
            total_bill = total_bill + (float(bill["BillDetails"][line_item]) * float(mstr_data[3]))

## exporting new json
bill["Total"]=total_bill
op_file = open(bill['BillID'] + "_with_totals.json", "w")
op_file.write(json.dumps(bill))

##closing files object
op_file.close()
f1.close()
f2.close()