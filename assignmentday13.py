
#Assignment 1
from configparser import ConfigParser
config = ConfigParser()
config.read("exc.ini")
print(config.sections())
print(config.options('EXT'))
import os

os.chdir(config.get("EXT","current_path"))

for file in os.listdir("."):
    
    if file.endswith(config.get("EXT","from")):
        first_name = file.rsplit(".",1)[0]
        new_name = first_name + config.get("EXT","to")
        print(new_name)
        os.rename(file,new_name)
        
"""
Assignment2
"""
import os
rep=os.walk("C:\\Users\\DELL\\Google Drive")
d1={}
for r,d,f in rep:
    for file in f:
        d1.setdefault(file,[]).append(r)
file_name=input('Enter the file name:')
for k,v in d1.items():
    if file_name.lower() in k.lower():
        for i in v:
            print(i)
            print('*'*50)
