# program to reverse the order of words 

s = input("Enter a string : ")
l = s.split()
l1 = []
i = len(l) - 1
while(i >= 0):
    l1.append(l[i])
    i = i-1
#print(l1)
output = ' '.join(l1)
print(output)