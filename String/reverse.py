s = input("Enter a string : ")
i = len(s) - 1
output = ''
while(i >= 0):
    output += s[i]
    i -= 1
print(output)