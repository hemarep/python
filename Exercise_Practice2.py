#recap
#String Slicing
"""
str1 = "abcdefghij"

print("string is : ",str1)

print("\nstring 'abcdefghij' start slicing on 2, ends on 10, skips every 2nd number inbetween ")
print(str1[2:10:2])#start :stop :Skip

print("String skips -1 = reversing")
print(str1[::-1])#reversing the string

#email program
#email_id = 'arun1.info@gmail.com' 
print("email_id is :") #getting user input 
email_id = input()


at_pos = email_id.find('@')
print("at_pos : ", at_pos)

rem_email = email_id[(at_pos+1):]
print(rem_email)

dot_pos = rem_email.find('.')
print("dot_pos : ", dot_pos)

domain = rem_email[0:dot_pos]
print("domain of this email id : ", domain)



#lists, sets, tuples, dictionary
#declaration, loops, project id program
#Lists
#declaration
list_var = ['Hema','Adhyu',5,10,50]
print(list_var)#prints all in single line
for list in list_var: #prints all in separate line
    print(list)

#tuples
#declaration
tuple_var = ("adithya","adhyu","hema",500,250,100.25,1000)
print(tuple_var)
for tuples in tuple_var:
    print(tuples)
    
    
#dictionary
#Key : Value pairs
dict_var = {"Mom":"Hema","Dad":"Arun",'Bro':'Adhyu',50:100,20:10}
print(dict_var["Mom"],dict_var[50])

"""

#Project_Id Program
#A list which has dictionary values and a list in the last dictionary value
#list in a dictionary 
Emp_dic = [{'emp_no' : 1001,
'emp_name' : 'Arun',
'emp_salary' : 150000,
'proj_id' : [101,102,105]},

{'emp_no' : 1002,
'emp_name' : 'Hema',
'emp_salary' : 120000,
'proj_id' : [101,103,104]},

{'emp_no' : 1003,
'emp_name' : 'Adhyu',
'emp_salary' : 150000,
'proj_id' : [101,103,105]}]

for Emp in Emp_dic:
    print(Emp)
    print("______")
    

#Display emp_name of employee whose proj_id is 101
#for Emp in Emp_dic:
#    print(Emp('proj_id'))
#print(proj_id)
#