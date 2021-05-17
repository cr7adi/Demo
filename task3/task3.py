#1. Create a list of 10 elements of four different data types like int, string, complex and float.
g = [1,2,"asdf",1+2j,1.2,3,3,3,3,4]
#2. Create a list of size 5 and execute the slicing structure 
v = [1,2,3,4,5]
print(v[::2])
#3. Write a program to get the sum and multiply of all the items in a given list.
l = [1,2,3,4,5]
sum=0
multiply=1
for i in range(len(l)):
    sum+=l[i]
    multiply*=l[i]
print("sum=",sum,"Multiply=",multiply)
#4. Find the largest and smallest number from a given list.
print(min(l),max(l))
#Create a new list which contains the specified numbers after removing the even numbers from a predefined list. 
l=[1,2,3,4,5,6,7,8,9]
odd = []
for i in l:
    if i%2!=0:
        odd.append(i)
print(odd)
#6. Create a list of elements such that it contains the squares of the first and last 5 elements between 1 and30 (both included).
square = []
for i in range(1,31):
    if i<6:
        square.append(i*i)
    elif i>25 and i<=30:
        square.append(i*i)
print(square)
# 7. Write a program to replace the last element in a list with another list

#a=list(a)
#b=list(b)
#a = [1,2,3,4]
#b=[1,2]
a,b = eval(input())
print(a,b)
print(a.pop(-1))

a.extend(b)
print(a)
#8 Create a new dictionary by concatenating the following two dictionaries:
a={1:10,2:20}
b={3:30,4:40}
a.update(b)
print(a)
#9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).
n = int(input("n="))
d = {}
for i in range(1,n+1):
    d[i]=i*i
print(d)
#10 Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number in the form of string.
i = input("numbers:")
x = filter(lambda x:x!=',',i)
y=list(x)
z= tuple(y)
print(y,z)
