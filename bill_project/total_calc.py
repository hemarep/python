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
f2 = open('/Users//arun//PycharmProjects//python//bill_project//new_bills//20221104232943.json', 'r')
bill = json.load(f2)

print(bill)

## total calculation
for line_item in bill["BillDetails"]:
    for mstr_data in prod_master_data:
        if line_item == mstr_data[0]:
            total_bill = total_bill + (float(bill["BillDetails"][line_item]) * float(mstr_data[3]))

## exporting new json

op_path = '//Users//arun//PycharmProjects//python//bill_project//output_totals//'

bill["Total"]=total_bill
op_file = open(op_path + bill['BillID'] + "_with_totals.json", "w")
op_file.write(json.dumps(bill))

print(bill)

##closing files object
op_file.close()
f1.close()
f2.close()

#91 89392 90389