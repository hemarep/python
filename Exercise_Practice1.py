#DAY6 Python Exercises
#Arun - 9 questions
#Employee Dictionaries

#question-1
#create a list with Proj_ids
#Emp_list =  [{'Proj_id' : [101,102,103,104,105]}]
Proj_ID = [101,102,103,104,105]

#question-2
#Print all in single line
#print("Proj_id'\s in the Emp_list are"+ Emp_list['Proj_id'])
print("Answer for 2")
print("Proj_id\'s in the list are", Proj_ID)
print("----------")


#question-3
#print eacch in loop
print("Answer for 3")
print("Each Proj_id\'s in the list are")
for id in Proj_ID:
     print(id)
print("----------")

#question-4
#create a dictionary of employee

Emp_dic = {'emp_no' : 100,
'emp_name' : 'Arun',
'emp_salary' : 150000,
'Proj_ID1' : [101,103,105]}


#question-5
#print key data of above dic
print("Answer for 5")
print("Emp_dic key and data values: ",Emp_dic)
print("----------")


#question-6
#print emp name,project 
print("Answer for 6")
#print(type(Emp_dic))
print("Emp_dic key and data values: ",Emp_dic['emp_name'], Emp_dic['Proj_ID1'])
print("----------")


#question-7
#create employee database list with dictionary

Emp_dic_db = [{'emp_no' : 10,
'emp_name' : 'Arun',
'emp_salary' : 150000,
'Proj_ID1' : [101,103,105]},
{'emp_no' : 11,
'emp_name' : 'Adhyu',
'emp_salary' : 170000,
'Proj_ID1' : [102,103,104]},
{'emp_no' : 12,
'emp_name' : 'Adithya',
'emp_salary' : 200000,
'Proj_ID1' : [102,103,104]}
]


#question-8
#print key data of above dic
print("Answer for 8")
print("Emp_dic key and data values: ",)
for Emp_db in Emp_dic_db:
    print(Emp_db)
print("----------")


#question-9
#print emp names of emp in proj 103
print("Answer for 9")
print("Employees in the project 103 are: ")
for Emp in Emp_dic_db:
    for Pid in Emp['Proj_ID1']:
        if Pid == 103:
            print(Emp['emp_name'],"\n")
print("----------")

