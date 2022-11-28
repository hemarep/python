#file handling
#file input-output

import os #importing os library

#getting current working directory cwd - os.getcwd()
cwd = os.getcwd()       
print("The current directory you're working on : ", cwd)

#Changing the directory - os.chdir()
ch_dir = os.chdir("c:\\test\\1")
print("Change the directory to: ",ch_dir)

#getting cwd after changing 
cwd = os.getcwd()       
print("The current directory you're working on : ", cwd)


#listing directory folders
#os.listdir()
print("Listing the folders in my working directory : \n\n",os.listdir())

#make new directory - os.mkdir()
new_dir = "C:\\test\\1\\make_file.txt"
#print("new_dir created is : ",os.mkdir(new_dir))

#printing the list after creating new folder
print("Listing the folders with newly added one : \n\n",os.listdir())

#folder exists 
print("Checking the existance of the new directory",os.path.exists(new_dir))

#removing 
print("removing the folder", os.rmdir(new_dir))
print(os.path.exists(new_dir))#checking after remove

