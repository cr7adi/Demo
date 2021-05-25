#1
import math
C=50
H=30
d = input("D:")
d= d.split(',')
q=[]
for D in d:
    Q= round(math.sqrt((2*C*int(D))/H))
    q.append(Q)
print(q)

#2
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

area_sq= Square(2)
print(area_sq.area())
print(Square().area())

#3
class Sum:
    def threesum(self,arr):
        result = []
        arr.sort()
        for i,j in enumerate(arr):
            if i>0 and j==arr[i-1]:
                continue
            l,r = i+1,len(arr)-1
            while l <r:
                threesum = j+arr[l]+arr[r]
                if threesum<0:
                    l+=1
                elif threesum>0:
                    r-=1
                else:
                    result.append([j,arr[l],arr[r]])
                    l+=1
                    while arr[l]==arr[l-1] and l<r:
                        l+=1
        return result
a = Sum()
print(a.threesum([-25,-10,-7,-3,2,4,8,10]))

                
                
                    


#4
class Time(object):
    def __init__(self,hours=0,mins=0):
        self.hours = hours
        self.mins = mins
    def addTime(time1, time2):
        result = Time(0,0)
        if time1.mins+time2.mins> 60:
            result.hours = int(time1.mins + time2.mins)//60
        result.hours = result.hours+time1.hours+time2.hours
        result.mins = (time1.mins + time2.mins)%60
        return result
    def displayTime(self):
        print("Time is:",self.hours, "hours and",self.mins,"minutes")
    def displayMinute(self):
        print((self.hours)*60+self.mins)
a = Time(2,40)
b = Time(1,30)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()
#5
class Person():
    age = 0
    def __init__(self,Age):
        if Age<0:
            print("Age is not valid, setting age to 0")
        else:
            self.age = Age
    def yearPasses(self):
        self.age+=1

    def amIOld(self):
        if self.age<13:
            print("You are young")
        elif self.age>=13 and self.age<=19:
            print("You're a teenager")
        else:
            print("Your'e old")
a =Person(100)
a.amIOld()