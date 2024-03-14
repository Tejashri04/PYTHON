s = 'Durga software solutions'

l = s.split()       # default seprator is space
print(l) 
print(type(l))

for x in l :
    print(x) 

l1 = s.split('s')
print(l1)
for x in l1 : 
    print(x) 

s2 = 'one,two,three,four,five,six'
l2 = s2.split()
l3 = s2.split(',')
print(l2)
print(l3)