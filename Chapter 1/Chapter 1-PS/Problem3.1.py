##write a python program to print the contents of a directory using the os module. search online Without comment

import os
#select the directory whose content you want to list

directory_path = '/'

#Use the os module to list the directory content
contents = os.listdir(directory_path)

#Print the contents of the directory
print(contents)
