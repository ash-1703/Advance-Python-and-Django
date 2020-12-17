"""shallow copy """
list=['xy',56,'z',100]
list1=['xyz',564,23,'a']
list2=list[:]
print(list)
print(list2)
print(id(list2))
print(id(list))

"""deep copy"""
from copy import deepcopy
list3=[['Aishwarya'],15,10,['Tupe']]
list4=deepcopy(list3)
print(list4)
list3.append(3)
print(list3)
print(list4)
list3[0].append('Sambhaji')
print(list3)
print(list4)
list4[0].append('Pratima')
print(list3)
print(list4)