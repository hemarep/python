#Data Structures in python
#Lists, sets, tuples, dictionary

#LISTS
#list is a keyword 
#Creating diff list types
#printing each type
#printing list by position = 'INDEX'

empty_list = [] 
int_list = [2,4,6,8,20,40]
string_list = ['A','H','Adithya',"Hello--","World!"]
print("Empty list:", empty_list)
print("int_list: ",int_list)
print("string_list: ",string_list)

compound_list = ['Hema','Adhyu',5,10,50,100.50,200]
print("Compound list in single line : ",compound_list)
print("______")

print("Displays in each line:")
for list in compound_list:
    print(list)
    
#printing list by index positions
#prints from right index value position 0 to all   
print("Printing list by index positions : ", compound_list[0:]) 
print(compound_list[-2]) #prints from second position from right
print(compound_list[3:6]) #ignores to print the index value after colon
print(compound_list[2:4]) #ignores after colon 
print(compound_list[5]) #prints 5th position value
print(compound_list[-1])

#Creating lists to use
list1 = ['Python','cobra','anaconda',5,50,100]
print("list1 : ",list1)

#inserting in the list
#inserting one element at the end = append()
list1.append(150)
print("list1 after appending at end : ", list1)

#inserting using index value
list1.insert(0,'code')
list1.insert(2,99)
print("list1 after inserting using index positions",list1)

#updating the list
#we can add multiple elements to the existing list
list1[0:2] = ["Om",'Sai','Ram']
print("list1 after updating : ",list1)


#Slicing concept in the list
list1_slice = list1[0:4]
print(list1_slice)
#print(list1.find("Om"))