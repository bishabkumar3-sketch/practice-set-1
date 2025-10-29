# Write a python program to print the contents of a directory using os module. Search online for the function which does not 
import os

directory_path = '/'

contents = os.listdir(directory_path)

for item in contents:
    print(item)