#Python Dictionary
#Dictionaries are associative arrays, unordered set of key:value pairs.
#Dictionaries declaration is in flower brackets
#d = {'Key1' : 'value1', 'Key2' : 'value2'} 
#Dictionaries keys can be any immutable type (Strings and Numbers)
#Dictionaries support conditional and iterative operations 
#Dictionaries have built-in functions and methods similar to strings


# Create empty Dictionary
dict0 = {}
print(dict0)

#Create dictionary with values
#Here both Key and Value are String
dict1 = {'key1':'Value1', 'key2':'Value2', 'key3':'Value3'}
print(dict1) # OUTPUT: {'key1': 'Value1', 'key2': 'Value2', 'key3': 'Value3'}

eats = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}
print(eats) # OUTPUT: {'OKRA': 'VEGITABLE', 'POTATO': 'ROOT', 'APPLE': 'FRUIT'}


#Adding and Modifying elements of a dictionary
#update 

add_dic = {'name':'hema','age':'30'} #created a dictionary
print(add_dic) #prints all in one line
add_dic.update({'relation':'mom','hobby':'gardening'}) #adding new values to it
print(add_dic)
add_dic.update({'job':['developer','tester']})
print(add_dic)
#printing each pair in separate line
for key, value in add_dic.items():
    print(key, value)

# Print a value of a key 
print(eats['POTATO']) # OUTPUT: ROOT

# Change a Keys value
eats['POTATO'] = 'VEGETABLE'
print(eats['POTATO']) # OUTPUT: VEGETABLE

# remove one element, key-name: POTATO
del eats['POTATO']

# remove all elements
eats.clear()

# delete dictionary
del eats

#print(eats) # This will result in error.

# Recreate eats
eats = {'APPLE':'FRUIT', 'POTATO':'ROOT', 'OKRA':'VEGETABLE'}

# Get all Keys, returns a list
print(eats.keys())
eats.keys

# Read all elements of a dictionary

for key, value in eats.items():
    print(key, value)
# OUTPUT
#    APPLE FRUIT
#    OKRA VEGETABLE
#    POTATO ROOT
## >```