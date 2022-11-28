import os

print(os.getcwd())
os.chdir("//Users/arun//test//")
print(os.getcwd())

nf = open("newfile.txt",'w')
for i in range(10):
    nf.write("this is line " + str(i)+ "\n")

print(nf.readlines())