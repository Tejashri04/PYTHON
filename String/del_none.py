# Difference between del and None

# 1
s1 = 'durga'
s2 = s1 
s3 = s1
del s1 
print("s2 : ",s2)
print("s3 : ",s3) 

# 2 
s4 = 'durga'
del s4 
#print(s4)      --->    Error : name 's4' is not defined 

# 3 
s5 = 'durga'
s5 = None
print("s5 : ",s5) 

# 4 
s6 = 'durga'
# del s6[0]  --->  str' object doesn't support item deletion
print(s6)
