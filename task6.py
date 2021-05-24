from functools import reduce


x = [i for i in input("input string:") if i.isupper()]
print(x)
y = {i:j for i,j in zip(['Smit', 'Jaya', 'Rayyan'],['CSE', 'Networking', 'Operating System'] )}
print(y)
def reverse(string):
    length = len(string)
    for i in range(length - 1, -1, -1):
        yield string[i]
z= reduce(lambda x,y:x+y,(x for x in reverse("Consultadd Training")))
print(z)
#decorater example
def hello():
    print("hello")
def dec(func):
    def another():
        print("hello again")
        def anotherone():
            print("hello again:>")
        return anotherone
    func()
    print("bye")
    return another
i = dec(hello)
j=i()
j()