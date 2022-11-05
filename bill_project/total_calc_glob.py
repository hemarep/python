import csv
import json
import glob
import shutil
import time

prod_master_data = []
total_bill = 0.0

## importing CSV
with open('products.csv','r') as f1:
    csv_data = csv.reader(f1)
    next(csv_data)
    for data in csv_data:
        prod_master_data.append(data)

run = True

while run:
    ## importing Json
    json_files = glob.glob("/Users//arun//PycharmProjects//python//bill_project//new_bills//*.json")

    for file in json_files:
        f2 = open(file, 'r')
        bill = json.load(f2)

        total_bill = 0.0
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

        print ("Total :", total_bill)

        old_path = "/Users//arun//PycharmProjects//python//bill_project//new_bills//" + bill["BillID"] + ".json"
        new_path = "/Users//arun//PycharmProjects//python//bill_project//processed_bills//" + bill["BillID"] + ".json"

        shutil.move(old_path,new_path)

    time.sleep(3)
    file_count = len(glob.glob("/Users//arun//PycharmProjects//python//bill_project//new_bills//*.json"))
    if file_count == 0:
        run=False

##closing files object
op_file.close()
f1.close()
f2.close()