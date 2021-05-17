x = str(input("enter a string:"))
Digits = Letters=0
for i in x:
    if i.isnumeric():
        Digits+=1
    if i.isalpha():
        Letters+=1
print("Digits:",Digits,"Letters:",Letters)