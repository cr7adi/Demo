x = int(input("Guess the lucky number:"))
count =1
while count<6:

    if x==6:
        print("good guess")
        break
    elif count==5:
        print("game over")
        break
    else:
        x = int(input("guess again:")) 
        print("you have",4-count,"guesses remaining")
        count+=1
        
