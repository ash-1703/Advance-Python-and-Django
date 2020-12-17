import os
import re
import time
t1=time.time()
dict={}
x=1
def get_drives():
  resp=os.popen("disk caption")
  drive=resp.read
  return drive.split()[1:]

def creatingindex(path):
  global x
  resp=os.walk(path)
  for root,d,files in resp:
    for files in file:
      path1=root+"\\"+gile
      print(path1)
      file1=file+"|"+str(x)
      dict1[file1]=path1
      x=x+1

def search(file1):
  for k,v in dict.items():
    k=k.split("l")[0]
    m=re.search(file1,k,re.l)
    if m:
      print(k,":",v)

for d in get_drives():
  print(d)
  creatingindex(d+"//")
t2=time.time()
print(t2-t1)
file1=input("Enter the file name")
search(file1)