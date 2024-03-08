# reverse the internal content of each word

s = input("Enter a string : ")
l = s.split()
l1 = []
for x in l :
    l1.append(x[::-1])
print(l1)
output = ' '.join(l1)
print(output)

