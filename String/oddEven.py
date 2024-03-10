# write a program to print characters at odd position and even position

# s = input("Enter a string : ")
# print("Chracters at even position : ",s[::2])
# print("Chracters at odd position : ",s[1::2]) 

# OR 

s = input("Enter a string : ")
print("Characters at even position : ")
i = 0 
while i < len(s):
    print(s[i],end=" ")
    i = i + 2
print()
print("Characters at odd position : ")
i = 1 
while i < len(s):
    print(s[i],end=" ")
    i = i + 2