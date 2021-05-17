#1. Create three variables in a single line and assign values to them in such a manner that 
#each one of them belongs to a different datatype.
a,b,c = 2,2.301,'abcs'
#2. Create a variable of type complex and swap it with another variable of type integer.
d = 1+2j 
print(type(d))
temp = a
a = d
d = temp
print(type(d))

#3. Swap two numbers using a third variable and do the same task without using any third variable.

d = 1+2j 
print(type(d))
a=2
temp = a
a = d
d = temp
print(d)
##without using any third variable
d = 1+2j 
a=2
d=a
print(d)

#4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.

#5. Write a program to complete the task given below: Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the 
#sum in another variable called z. Add 30 to z and store the output in variable result and print result as the final output.

x,y= input("enter any 2 numbers in between 1-10:").split()
z= int(x)+int(y)
z=z+30
print(z)


#6. Write a program to check the data type of the entered values.
x = input("enter any 2 numbers in between 1-10:")
print(type(x))

#7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.
v = "Example"
v1 = "example"
v2 = "example"
v3 = "EXAMPLE"

#8 If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change 
#the value? 

#yes once the different data type value assigned to same variable 'a' then the initial value which is stored in the memory value  is 
#replaced with the new value which is assigned to the same variable.


