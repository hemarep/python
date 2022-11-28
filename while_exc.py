#WHILE LOOP, Iterate as long as a condition is true and exit when the
#condition is false 
#PYTHON LOOP CONTROL: BREAK Statement
#PYTHON WHILE LOOP
#PYTHON LOOP CONTROL: CONTINUE Statement
#PYTHON LOOP CONTROL: PASS Statement

# The below syntax loops until curr_value reaches 5
# looping 5 times using while loop 
curr_value = 0                  # SETUP a condition criteria
while (curr_value < 5):
    curr_value += 1  # same as curr_value = curr_value + 1
    print('Curr_value: ', curr_value)    


# INFINITE LOOP issue
# great care should be taken when writing loops as it could iterate perpetually or
# run in an infinite loop,while some situations require to run forever like services

# CODE
#  while(1==1)
#      print("in infinite loop")



# Using break with while loop
cur_value = 0                  # SETUP a condition criteria
while (cur_value < 5):
    cur_value += 1  # same as curr_value = curr_value + 1
    if cur_value==3:
        break
    print('Cur_value: ', cur_value)    



"""
while True:
    print("email_id is :") #getting user input 
    email_id = input()
    if email_id.find('@') > 1:
        break

at_pos = email_id.find('@')
print("at_pos : ", at_pos)

rem_email = email_id[(at_pos+1):]
print(rem_email)

dot_pos = rem_email.find('.')
print("dot_pos : ", dot_pos)

domain = rem_email[0:dot_pos]
print("domain of this email id : ", domain)

"""