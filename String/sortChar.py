# Write a program to sort characters present in the given string.First alphabet symbols & then numeric values

s = "B4A1D3"
s1 = s2 = ""
for x in s : 
    if x.isalpha():
        s1 = s1 + x 
    else :
        s2 = s2 + x 

output = ''
for x in sorted(s1):
    output = output + x
for x in sorted(s2):
    output = output + x 
print(output) 