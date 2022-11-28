#File_handling in python
#reading,open,close,write
"""
import os

#open a file in read mode
#only read "r"
#opens

input_file = open("C:\\Users\\hema1\\Documents\\Python notes\\keys_tips.txt","r") 

text_file = input_file.read() #reads everything when opens
print(text_file)

input_file.close()#close the file

print("\n This is a python file")
print("opening and reading the text file \- keys tips & then closing, coming back to file handling")
"""

"""
#read the file line by line

#opening 
#reading line using function readline()
#closeing

import os

input_file = open("C:\\Users\\hema1\\Documents\\Python notes\\keys_tips.txt","r") 

while True:
    current_line = input_file.readline()
    
    if not current_line:
        break
    print(current_line)

input_file.close()#close the file
"""

#reading the line"s" without loop = prints lists
#readlines()
"""
import os

input_file = open("C:\\Users\\hema1\\Documents\\Python notes\\keys_tips.txt","r")

text_file = input_file.readlines()
print(text_file)

input_file.close()

print("\n This is coming back to python after reading the line\'s from text file")
print("Which results printing in lists")
"""

#Writing in a file "w"
#opening,wrinting,closing

output_file = open("C:\\Users\\hema1\\Documents\\Python notes\\keys_tips.txt","w") 

output_file.write("File handling concepts in python_1")
output_file.write("\nWriting thru python file_1")
output_file.write("\nOpens, write these lines, closes_1")
output_file.close()


output_file1 = open("C:\\Users\\hema1\\Documents\\Python notes\\keys_tips.txt","r") 
read_output = output_file1.read()

print(read_output)

output_file1.close()#close the file

#print("\n This line comes backs to python file")
#print("opening and reading the text file \- keys tips & then closing, coming back to file handling")
