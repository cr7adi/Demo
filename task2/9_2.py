x = input("Guess the lucky number:")
number = 6
answer = "no"
print(type(x),type(answer))
while(True):
    if x==str(number):
        break
    elif x==answer:
        break
    else:
        x = input("do u want to guess again:")
