'''
x=123
print(type(x))
for i in x:
    print(i)
'''
# Answer : TypeError: 'int' object is not iterable
'''
i=0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")
'''
#Answer 
'''
0
error
1
error
2
'''
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break
#NameError: name 'Break' is not defined