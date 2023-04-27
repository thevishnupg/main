# Area of a rectangle

# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def Area(self):
#         area = self.width * self.height
#         return area
# n = int(input('Enter the widht:'))
# m = int(input('Enter the height:'))

# rect = Rectangle(n,m)
# print(rect.Area())

#############################################

# Create a circle class and initialize it with radius. Make two methods getArea and getCircuference inside this class

# class Circle:
#     def __init__(self,radius):
#         self.rad = radius
    
#     def getArea(self):
#         area = (self.rad**2)*3.14
#         return area
#     def getCircumference(self):
#         circumference = (self.rad)*(2*3.14)
#         return circumference

# x = int(input('Enter the radius:'))

# cir = Circle(x)

# print('Area of a circle is:',cir.getArea())
# print('Cicumference of a circle is:',cir.getCircumference())

######################################################

# To convert fahrenheit to celcius and vice versa

# class Temperature:
#     def __init__(self,temp):
#         self.temp = temp

#     def ConvertFahrenheit(self):
#         far = (self.temp-32)*(5/9)
#         return far
    
#     def ConvertCelcius(self):
#         cel = (self.temp*(9/5))+32
#         return cel
# x = int(input('Enter the temperature:'))

# tem= Temperature(x)
# print('Fahrenheit to Celcius is :',tem.ConvertFahrenheit())
# print('Celcius to Fahrenheit is :',tem.ConvertCelcius())

############################################################

# Create a student class and initialize it with name and roll noumber. Display info, assign age, and mark

# class Student:
#     def __init__(self,name,roll):
#         self.name = name
#         self.roll = roll
    
#     def Age(self):
#         a = int(input('Enter the age:'))
#         return a
    
#     def mark(self):
#         m = int(input('Enter the mark:'))
#         return m
    
#     def Info(self):
#         nam = 'Name of student:',self.name
#         rol ='Roll no of student:', self.roll
#         ag = 'Age of student:',self.Age()
#         mrk = 'Mark of student:',self.mark()
#         return nam , rol,ag,mrk
    

    
# student1 = Student(input('Enter the name:'),int(input('Enter the roll number:')))

# for i in student1.Info():
#     print(i)

#####################################################################

# Create a time class and initialize it with hours and minitues then :-
# make a methode AddTime which should take two time object and add them..
# make a methode DisplayTime which should print the time..
# make a methode DisplayMintue which should display the total minitues in the time.

# class Time:
    
#     def __init__(self,hours,minutes):

#         self.hours = hours
#         self.minutes = minutes

#     def AddTime(self):
#         a = self.hours
#         b = self.minutes
#         c = (a*60) + b
#         return c
    
#     def DisplayTime(self):

#         print(self.hours,'hour',self.minutes,'minutes')

#     def DisplayMinutes(self):

#         a = self.hours
#         b = self.minutes
#         c = (a*60) + b
        

#     def __add__(self,other):

#         a = (self.hours*60)+(other.hours*60)
#         b = self.minutes+other.minutes

#         c= (a+b)//60
#         d = (a+b)%60
#         e = Time(c,d)
#         return e

# print()
# print('Enter the time for first object')
# print()
# x = int(input('Enter the hours:'))
# y = int(input('Enter the minutes:'))
# print()
# print('Enter the time for second object')
# print()
# p = int(input('Enter the hours:'))
# q = int(input('Enter the minutes:'))
# print()

# timeobject1 = Time(x,y)
# timeobject2 = Time(p,q)

# timeobject1.DisplayTime()
# timeobject1.DisplayMinutes()

# timeobject2.DisplayTime()
# timeobject2.DisplayMinutes()

# timeobject3 = timeobject1+timeobject2

# print(timeobject3.hours,'hour',timeobject3.minutes,'minutes')
#####################################################################

