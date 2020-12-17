import datetime
main_list = list(range(100000))
t1 = datetime.datetime.now()
list1 = (each**2 for each in main_list)
for each in list1:
  each
t2 = datetime.datetime.now()
print (t2-t1)

"""
"""
import datetime
main_list = list(range(100000))
t1 = datetime.datetime.now()
list1 = (each**2 for each in main_list)
for each in list1:
  each
t2 = datetime.datetime.now()
print (t2-t1)

"""
"""

import datetime
main_list = list(range(10000000))
t1 = datetime.datetime.now()
list1 = (each**2 for each in main_list)
for each in list1:
  each
t2 = datetime.datetime.now()
print (t2-t1)