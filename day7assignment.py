list1=[10,20,30,40,50]
list2=[5,15,25,35,45,60]
list3=list1+list2
sorted_list=[]
while list3:
    mini=list3[0]
    for item in list3:
        if item<mini:
            mini=item
    sorted_list.append(mini)
    list3.remove(mini)
print(sorted_list)    