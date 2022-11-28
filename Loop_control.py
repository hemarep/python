#Python FOR loop 
#Loop Control statements

#python iterative or for loop, 
#while loop, loop control, break, continue, pass

# PYTHON ITERATIVE or LOOPS
# When a piece of code need to be executed repeatedly, 
# LOOP construct is used.
# Python provides `TWO` loops **FOR LOOP** and **WHILE LOOP**
# NESTED FOR LOOP over number of characters in a string


# PYTHON FOR LOOP
#FOR LOOP, Iterate over a SEQUENCE type (Lists, Tuples, Dictionaries) 
#or Range of numbers
#FOR LOOP over a list
#FOR LOOP over a subset of list
#FOR LOOP over a range of numbers
#FOR LOOP over number of characters in a string

#Loops 5 times
for c in range(5):
    print('Loop Count: ',c) # Index starts from ZERO !

#LOOP Over the number of characters in a sting
for character in 'MyString':
    print(character) # Prints all the characters in new line

# SYNTAX 1: LOOP over elements in a LIST
print("/n Looping the list: ")
myList = [1, 2, 3, 4, 5]
for element in myList:
    print(element)  
    
# SYNTAX 2: LOOP over elements in a LIST
print("\n Loop for range of len of list: ")
for element_index in range(len(myList)):
    print(myList[element_index])  
    
    
# Loop through a sub set of list of elements
print("\n Loop thru subset of the list: ")
for element in myList[2:4]:
    print(element)  

# Nested Loops (loop inside loop)
#for each index of outer loop, there prints the full row of inner loop
print("\n Loop inside loop, for each outer loop there's a inner loop")
for outer_loop in range(5):
    for inner_loop in range(2):
        print('outer_loop-inner_loop', outer_loop, '-', inner_loop) 
       

#PYTHON LOOP CONTROL BREAK Statement
#Break clause is used to terminate/exit a loop before loop execution is complete

# The following loop exits before 5 iterations
print("\n 'Break' exit the loop:  ")
for c in range(5):
    if c == 3:
        break
    print(c) #doesnt print after break 


#CONTINUE Statement
#continue clause ignores all the remaining statements 
#in the current loop iteration and takes control 
#back to the first step in a next loop iteration (if any left)
print("\n 'Continue' end the current loop and continues back to previous loop")
for c in range(3):
    print('Run:', c,'step1')
    if c==1:
        continue 
    print('Run:', c,'step2')
    print('Run:', c,'step3')

# OUTPUT
#        Run: 0 step1
#        Run: 0 step2
#        Run: 0 step3
#        Run: 1 step1    # Didnt print step2 and step3
#        Run: 2 step1
#        Run: 2 step2
#        Run: 2 step3


#PASS Statement
#When no action is needed use pass, as it does nothing
#This is very useful as a placeholder for future code
print("\n 'PASS' acts as a placeholder for future code")
for c in range(3):
    if c==1:
        print('Do a very important step')
    elif c==2:
        pass # DO NOTHING
    else:
        print('normal processing')


"""
for a in range(5):
    break
	print (a)
"""