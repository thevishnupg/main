#Question1: Program to find area, perimeter of a rectangle using function.

#Question2:  Programe to convert celcius to farenheat and vice versa using function.

#Question3:  Program to find sum of a list using function.



# Question 1 

# def area(x,y):
#     a = x
#     b = y 
#     c = a*b
#     return c 

# def peri(x,y):

#     m = x
#     n = y 
#     o = 2*(m+n)

#     return o
    

# length = int(input('Enter the length of rectangle:'))
# width = int(input('Enter the width of rectangle:'))

# result1 = area(length,width)
# result2 = peri(length,width)

# print('Area of rectangle is :',result1)
# print('Perimeter of rectangle is :',result2)

######################################################################

# Question2


# def cel_to_far(x):

#     c=x
#     c=(float(c))
#     far = (c*(9/5))+32
#     return far

# celcius = float(input('Enter celcius :'))
# result1 = cel_to_far(celcius)
# print('Celcius to Farenheat :',result1)


# def far_to_cel(y):

#     f=y
#     f=(float(f))
#     cel = (f-32)*(5/9)
#     return cel

# farenheat = float(input('Enter farenheat:'))
# result2 = far_to_cel(farenheat)
# print('Farenheat to Celcius :',result2)

#####################################################################


# Question3


# def sum_of_list(x):
#     k=0
#     a=x
#     for i in a:
#         c = i
#         c = float(c)
#         k = k+c
#     return k


# lis = [2,2,2,2,2,2]

# result = sum_of_list(lis)
# print(result)
#######################################################################


# def account(name, acc, bal):
#     a =name
#     b = acc
#     c = bal
#     balance=bal
#     option= int(input('Select your option: 1 or 2 or 3 or 4 :'))

#     if option==1:

#         def dep():
#             balance=bal
#             d = int(input('Enter how much do you want to deposit :'))
#             balance = balance+d
#             return balance

#         res1 = dep()
#         print('Deposit successfull')
#         print('Your current balance is : ',res1)
#         print()
#         print('Thankyou')

#     elif option==2:

#         def wit():
#             balance=bal
#             w = int(input('How much do you want to widrow :'))
#             print(w)
#             balance= balance-w
#             return balance

#         res2 =wit()
#         print('Withdrowel successfull')
#         print('Your current balcence is : ',res2)
#         print()
#         print('Thankyou')
        

#     elif option==3:

#         def baln():
#             balance=bal
#             print('Your balcne is :',balance)
#             print('Thankyou')

#         baln()

#     elif option==4:

#         def ext():
            
#             print('Thank you')

#         ext()

#     else:
#         print('something went wrong')
#         print('Thankyou')
        
#     return a ,b , c


# print('option 1:- deposit')
# print('option 2:- withdrowel')
# print('option 3:- balance')
# print('option 4:- exit')    

# print()
# print()

# result= account(input('Enter your name:'), int(input('Enter your account number:')),bal=100000)



