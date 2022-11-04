"""
# Generate list with squares
list_1 = [5, 6, 7]

# list comprehension
new_list = [c*5 for c in list_1]
print(new_list)

# MAP Single Function with an Iteration with Lambda
y = list(map(lambda v : v * 5, list_1))
print(y)

# MAP Multiple Functions with an Iteration with Lambda
def Add2(x):
        return (x+2)
def Add3(x):
        return (x+3)

MyFunctions = [Add2, Add3]

for num in range(5):
    data = list(map(lambda x: x(num), MyFunctions))
    print(data)
    data1=[c(num) for c in MyFunctions]
    print(data1)
    print("-----------")
"""

# FILTER Function
# Removes list of a values that dont match the criteria
# Create a List of Even Numbers Only
evenList = list(filter((lambda x: x%2 == 0), range(10)))
print(evenList)

# Create a List of Salary only > 1000
salary_list = [100, 2000, 300, 4000]

list_1000_PLUS = list( filter((lambda x: x>1000), salary_list))
print(list_1000_PLUS)

#Accepts a function and list of values to return a single value
#by processing the result over and over untill a single value remains
from functools import reduce

addData = reduce((lambda x,y:x+y),range(10))
print(addData)

mulData = reduce((lambda x,y:x*y),range(1,10))
print(mulData)

