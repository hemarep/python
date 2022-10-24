# Generate list with squares
list_1 = [5, 6, 7]

# list comprehension
new_list = [c*5 for c in list_1]
print(new_list)

# MARKDOWN
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

