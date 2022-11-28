#Strings samples in python
#String Arrays
#string slicing
#string methods
#find,index 

#String variable declare/assign
String1 = 'Hello'
String2 = ("""My name is hema.
I am a python developer,
and a quality assurance tester, an analyst, 
and a data science engineer,
and a mom
and a homemaker,...""")


print(String1)
print(String2)
print("___________")
#SLICING

#printing each character in the string = indexing/positioning
#finding character using its position 


string_var = "Python is easy to learn"
print(string_var[0])#P 
print(string_var[5])#from left to right = n
print(string_var[6])#space
print(string_var[-1])#prints from right to left
print(string_var[-5:])
print(string_var[0:6])
print(string_var[0:9])
print(string_var[-5:-1])


#printing the position of the string using the character = find()
#finding using the character

string_find = "Python Strings is easy to learn"
print(string_find.find('P'))#prints the position number
print(string_find.find('y'))
print(string_find.find('s'))#lowercase s position = 13
print("----------")

#exercise 
#using above methods of slicing = find,index 
#requirement to find the domain in the email address


#my-sample-1
email = "hema14it@gmail.com"

at_pos = email.find('@')
print(at_pos)

dot_pos = email.find('.')
print(dot_pos)

domain = email[(at_pos + 1): dot_pos]
print("domain =", domain)
print("_________")



#my-sample-2
#email with two dots

email2 = "m.arunshankargmail@yahoo.com"
print(email2)

at_pos2 = email2.find('@')
print("at_pos2 = ", at_pos2)

rem_email = email2[(at_pos2+1):]
print("rem_email = ", rem_email)#prints half email = after @

dot_pos2 = rem_email.find('.')
print("dot_pos2 = ", dot_pos2)

domain2 = rem_email[0 : dot_pos2]
print("domain2 =", domain2)


#my-sample-3
#email3 = test@design


# String Methods And Functions
print("\n _________STRING METHODS________\n")
## >### String Methods - Text Case conversion
## >```
# Testing String
var_string_case_test = "learn PYTHON"

# upper case conversion
print(var_string_case_test.upper()) # OUTPUT:  LEARN PYTHON

# lower case conversion
print(var_string_case_test.lower()) # OUTPUT:  learn python

# title case conversion
print(var_string_case_test.title()) # OUTPUT:  Learn Python

# swap case conversion, swaps upper to lower and vice versa
print(var_string_case_test.swapcase())  # OUTPUT:  LEARN python

# capitalize case conversion, UPPERs the first letter of the string
print(var_string_case_test.capitalize())  # OUTPUT:  Learn python
## >```

print("\n _________STRING METHODS CHECKING ________\n")
## >### String Methods - Checking methods
## >```
# The Checking methods print true or false (Boolean)
# Checking if the string is UpperCase
print ('PYTHON'.isupper())   # prints true

# Checking if the string is lowerCase
print ('PYTHON'.islower())   # prints false

# Checking if the string is alphabets only
print ('PYTHON01'.islower()) # prints false

# Checking if the string is alphnumeric (alphabets/digits)
print ('PYTHON01'.isalnum()) # prints true

# Checking if the string is alphnumeric (alphabets/digits/special characters)
print ('1000'.isnumeric()) # prints true

# Checking if the string is white space (space/tab)
print ('  '.isspace()) # prints true
## >```


## >### String Methods - String Manipulation
## >```
# remove parts of string
# and return the changed string

# strip() Removes the white spaces before and after the string
print (' This is a test  '.strip())
# OUTPUT: This is a test

print ('This is a test'.strip('t')) # removes the last occurrence of 't'
# OUTPUT: This is a tes

print ('This is a test'.strip('T')) # removes the last occurrence of 'T'
# OUTPUT: his is a tes

print ('This is a test'.lstrip('This')) # removes the last occurrence of 'This'
# OUTPUT:  is a test

# lstrip() Removes the leading characters or white spaces by default 
# white spaces, of a string
# Removes the white spaces before and after the string
print (' This is a test  '.lstrip())
# OUTPUT: This is a test
print ('This is a test  '.lstrip('This'))
# OUTPUT: is a test  

# rstrip() Removes the trailing characters or white spaces by default 
# white spaces, of a string
# Removes the white spaces before and after the string
print ('This is a test  '.rstrip(' test'))
# OUTPUT: This is a
## >```


## >### String alignment justify
## >```
# ljust, center, rjust
# justify methods that add white spaces by default to
# align the string, and pad the string to the length mentioned
print ('test'.ljust(10,'+'))
# OUTPUT: test++++++
print ('test'.rjust(10,'+'))
# OUTPUT: ++++++test
print ('test'.center(10,'+'))
# OUTPUT: +++test+++
## >```


## >### Work with portions of string
## >```
# find()/index(): displays the position index of a given substring and 
# its occurrence number
print ('test'.find('t',2)) # print the index of the second occurrence of 't'
# OUTPUT: 3

print ('test'.index('t')) # print the index of the first occurrence of 't'
# OUTPUT: 0

# find() does not raise error, it returns -1 when not found
print ('test'.find('z')) 
# OUTPUT: -1

# index(), raises an error when not found
# print ('test'.index('z')) 
# ERROR: ValueError: substring not found

#rfind(), prints the highest index and -1 when not found
print ('test'.rfind('z')) # OUTPUT: -1
print ('test'.rfind('t')) # OUTPUT: 3

#rindex(), prints the highest index and errors out when not found
print ('test'.rindex('t')) # OUTPUT: 3

#replace(); replace the characters with the specified characters 
print ('test'.replace('t','i')) # OUTPUT: iesi


#split(), This converts a string into a list based on a separator, 
#default is whitespace 
print('This is a test'.split()) # prints a LIST, seperated by a whitespace
print('This|is|a|test'.split('|')) # prints a LIST,  seperated by a pipe |
print('This,is,a,test'.split(',')) # prints a LIST,  seperated by a comma ,

#splitlines(), Converts multi-line strings to a list
# Test varaible with multi-line string
testString = """Line 1
Line 2
Line 3
"""
print(testString.splitlines()) # OUTPUT: ['Line 1', 'Line 2', 'Line 3']
## >```