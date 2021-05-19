x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
#1)
print(x[5][:4])
print(x[6:8])
print(x[::-1])
print(x[5][5][:1])
print(x[:0])
y = range(1,1000,1)
#z = xrange(1,1000,1)
#the main difference being that lists are mutable while tuples are immutable. A list has a variable size while a tuple has a fixed size. Operations on tuples can be executed faster compared to operations on lists.
z= [i for i in range(1,100) if i%3==0 and i%2==0] 
print(z)
reverse = "alphabet"
#reverse = [i for i in reverse[::-1]  if i!="a" and i!="e" and i!="i" and i!="o" and i!="u"]
reverse = [i for i in reverse[::-1]  if i not in "aeiou"]
index = [i for i,j in enumerate(reverse)]
print(index,reverse)
even = "hello my name is abcde"
even_len = [i for i in even.split() if len(i)%2==0]
print(even_len)
x = [1,2,3,4,5,6,7,8,9,-1]
x = [(i,j) for i in x for j in x if i+j==8]
print(x)
even_list,odd_list=[],[]
count = 0
n= int(input("enter number b/w 1-50:"))
while(count<9):
    if n%2==0 and len(even_list)<=5:
        even_list.append(n)
        n= int(input("enter number b/w 1-50:"))
    elif n!=0 and len(odd_list)<=5:
        odd_list.append(n)
        n= int(input("enter number b/w 1-50:"))
    count+=1
print(even_list,odd_list,max(sum(even_list),sum(odd_list)))   
occurence = input("enter string:")
#occurence = "12abcbacbaba344ab"
alpha =[i for i in occurence if i.isalpha()]
occurence = [[i,alpha.count(i)] for i in set(alpha)]
print(occurence)
'''
for i in occurence:
    if i.isalpha():
        alpha.append(i)
'''
tuple1=(1,2,3,4,5,6,7,8,9,10)
even_tuple = [i for i in tuple1 if i%2==0]
print(tuple(even_tuple))
