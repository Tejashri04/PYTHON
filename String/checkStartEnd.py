# Checking Starting and Ending part of a String

s = 'learning python is very easy'

print(s.startswith('l'))
print(s.startswith('L'))
print(s.startswith('learning '))
print(s.startswith('learning python'))
print(s.startswith('learning python is'))
print(s.startswith('learning python is very'))
print(s.startswith('learning python is very easy')) 

print()

print(s.endswith('learning python'))
print(s.endswith('easy'))
print(s.endswith('very easy'))
print(s.endswith('is very easy'))
print(s.endswith('python is very easy'))
print(s.endswith('learning python is very easy'))