#python print statement Practice
#python training day 1 practicals
#printing variables and operators

print("Printing Statement in python")

print("single line comments uses #")#single line comments

"""Multi line comments 
  inside triple 
quotes"""

print("Multi line comments uses double quotes")

"""
printing integer,char,string,append = +,comma = space ,escape \ char for special characters,
datatypes such as %, .format, declare variable names, 
* = multiplies the datatypes ,
unicode,
del,
arithmatic operators,
augmented operaters
"""
print(5,10,15) #printing integers without quotes, 'comma' creates empty space
print('"Printing String data inside single quotes"')
print('String inside single quotes')
print(2.5)

print('String one' + 'appended with String')
print('String one comma','string two creates space inbetween')

print('special characters printed with backslash \' \\ inside single quotes ')


a=2.4444
print(type(a))#prints the datatype of the variable
print("String datatype =%s Integer datatype =%5.1f" % (a,5))
#print("String datatype =%s Integer datatype =%5.1f" (5,a))

print("{0},{1},{2}".format("orange",2.5,5))


d = 25
print(d+5)
del d
print(d)
#arithmetic operaters
x = 10
y = 5
z = 2

print(x + y + z)#adds

print(y%z)#prints 5%2=1 remainder

print(y/z)#prints 5%2=2.5 quotient

print(11*11)#multiplies

print(11**2)#prints the power/exponential 11 to the power of 2

#augmented operaters
x += 10 #adds x+10 and assigns the value to x 
print(x)#x=20

y *= 5
print(y)






