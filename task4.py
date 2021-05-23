reverse = input("input string:")
print("reversed string",reverse[::-1])
def func(string):
    upper = sum(i.isupper() for i in string)
    lower = sum(i.islower() for i in string)
    print("No. of Uppercase characters :",upper,"No. of Lowercase characters :",lower)
 
func(input("input:"))
def unique(list):
    uni = [i for i in set(list)]
    return uni
x=unique(eval(input("list:")))
print(x)
hyphen = [i for i in input("input list:").split('-')]
hyphen.sort
print('-'.join(hyphen))
upper = input("input sentence:").upper()
print(upper)

def sum(n1,n2):
    print("sum=",int(n1)+int(n2))
sum(input("n1:"),input("n2:"))

def stringlength(s1,s2):
    if(len(s1)>len(s2)):
        print(s1)
    elif(len(s2)>len(s1)):
        print(s2)
    elif(len(s1)==len(s2)):
        print(s1)
        print(s2)
stringlength(input("s1:"),input("s2:"))

def squares():
    x = [i*i for i in range(1,21)]
    print(tuple(x))
squares()

def showNumbers(limit):
    for i in range(int(limit)+1):
        if i%2==0:
            print(i,"EVEN")
        else:
            print(i,"ODD")
showNumbers(input("limit:"))

x = filter(lambda x:x%2==0,[i for i in range(1,21)])
print(list(x))

x = list(map(lambda x:x*x ,filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10])))
print(x)

def func_execpt():
    try:
        x=5/0
    except:
        print("there is an Zero division error")
    else:
        print("5/0=:",x)
    finally:
        print("done")
func_execpt()

from functools import reduce
x = reduce(lambda x,y:str(x)+str(y),[1,2,3,4,5,6,7])
print(x)

def div(x):
    if x%3!=0 and x%7==0:
        return x
y = filter(div, range(1,100))
print(list(y))


multi = map(lambda x:x*x,[1,2,3,4,5,6,7])
print(list(multi))

#16) (i)2 ,(ii)  name 'f' is not defined
