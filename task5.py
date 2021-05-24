import sys

#1


try:
    eval("x=2")
except SyntaxError:
    print("handled by SyntaxError")

#2
try:

    with open(sys.argv[1], 'r') as my_file:
        print(my_file.read())
except:
    print("Enter filename again")


#3
try:
    assert len(input("enter number:"))==4
    print("nice")
except:
    print("The length is too short/long !!! Please provide only four digits")

#4
count =0
while count< 3:
    try:
        if input("username:")=="abcd":
            pass
        assert input("password:")=="1234"
    except:
        print("enter password again")
    else:
        print("welcome")
        break
    count+=1

#6
with open('doc.txt') as f:
    mylist = f.read().splitlines() 
mylist = [i for i in mylist if len(i)%2==0]
print(mylist)