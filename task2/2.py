num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))


result = 0
operation = int(input("enter number:"))
if operation==1:
	result = num1 + num2
elif operation==2:
	result = num1 - num2
elif operation==3:
	result = num1/num2
elif operation==4:
	result = num1*num2
elif operation==5:
	result = (num1 + num2)*(0.5)

if result<0:
	print("NEGATIVE ",result)
else:
	print(result)


