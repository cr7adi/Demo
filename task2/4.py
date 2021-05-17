x = int(input("enter number:"))
for i in range(4):
	if x<0:
		break
	print("It’s Over")
	if x>0:
		continue
	print("Good Going")