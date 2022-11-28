#master_data = {"prod_id":1,"prod_cat":"Frozen","prod_name":"Ice Cream", "unit_price":2.5}
master_data = [{"prod_id":1,"prod_cat":"Frozen","prod_name":"Ice Cream", "unit_price":2.5},
               {"prod_id":2,"prod_cat":"Frozen","prod_name":"Green Peas", "unit_price":2},
               {"prod_id":3,"prod_cat":"Frozen","prod_name":"Corn", "unit_price":5},
               {"prod_id":4,"prod_cat":"Frozen","prod_name":"Meat", "unit_price":4},
               {"prod_id":5,"prod_cat":"Frozen","prod_name":"Pizza", "unit_price":6}]

inp_prd_id = int(input("Enter the Product ID :"))
inp_qty = int(input("Enter the quantity :"))

for data in master_data:
    #print (data["unit_price"])
    if inp_prd_id == data["prod_id"]:
        print("your total is ", inp_qty * data["unit_price"])


    # if inp_prd_id==(master_data["prod_id"]):
    #     print("your total is ",inp_qty*master_data["unit_price"])
    #     run=False
    # else:
    #     inp_prd_id = int(input("Product id is not in the list, please enter correct ID: "))






    #if i["prod_id"]=inp_prd_id:
    #    print(str(i["unit_price"]))

