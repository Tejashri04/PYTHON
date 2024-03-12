# Finding substrings

s = 'Learning python is very easy'
print(s.find('python'))        # returns index of first occurrence of given substring

print(s.find('Python'))       # returns -1 if it is not avilable

print(s.find('Java'))          # returns -1 if it is not avilable

print(s.find('python',6,9))    # search from begin : 6 to end-1 : 8

print(s.find('p',6,10))  

print(s.find('python',6,10))

print(s.find('python',15,25))