d1={'Nick Fury': 'Tony Stark,Maria Hill,Norman Osborn','Hulk':'Tony Stark,HawkEye,Rogers', 'Rogers':'Thor','Tony Stark':'Pepper Potts,Nick Fury','Agent-13':'Agent-X,Nick Fury,Hitler','Thor':'HawkEye,Black Widow','Black Widow':'HawkEye','Maria Hill':"Hulk,Rogers,Nick Fury",'Agent-X':"Agent-13,Rogers", 'Norman Osborn': "Tony Stark,Thor"}
print(d1,'\n')
print('Output : \n')
value=[]

l1=list(d1.keys())
l2=list(d1.values())
l3=set(l1)
def splitvalues(l):
    return l.split(',')

for each in l2:
    value.extend(splitvalues(each))


l1.extend(value)

s1=set(l1)
v111=[]
keys=['Nick Fury']

def findhydra(k):
    v111.extend(splitvalues(d1[k]))
    
        
for k,v in d1.items():
    if k in keys:
        keys.extend(splitvalues(d1[k]))
kl=set(keys)
y=l3.intersection(kl)

for i in y:
    findhydra(i)

v222=set(v111)
print(s1-v222)