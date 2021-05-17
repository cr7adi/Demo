#3. Write a program to get the sum and multiply of all the items in a given list.
l = [1,2,3,4,5]
sum=0
multiply=1
for i in range(len(l)):
    sum+=l[i]
    multiply*=l[i]
print("sum=",sum,"Multiply=",multiply)
