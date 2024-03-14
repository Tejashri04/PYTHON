s = 'Learning python is very difficult'

s1 = s.replace('difficult','easy')
print("s : ",s)
print("s1 : ",s1)

s2 = s.replace(" ","")
print("s : ",s)
print("s2 : ",s2)

s = s.replace('difficult','easy')
print("s : ",s)

Str = ' abc abc ab abc a'
s3 = Str.replace(' ','')
print("Str : ",Str)
print("s3 : ",s3)
print(len(Str) - len(s3))

