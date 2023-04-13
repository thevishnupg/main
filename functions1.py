# ________________functions_______________
# _________________syntax_________________
# def functionname()
#       statements:
#       dkihfdifji
#       fkgjfdlldj
#       fdjfjahiod
#       dfjfwaojgf
# functionname() 





# _______Method one____
# def add(a,b):    
#     A = a
#     B = b
#     sum = A+B
#     print(sum)
# add(2,3)  




# _____Method two_____
# def add():    
#     a = int(input('Enter a number:'))
#     b = int(input('Enter a number:'))
#     sum = a+b
#     print(sum)
# add()





# _______Method three______
# def add(a,b):    
#     A = a
#     B = b
#     sum = A+B
#     return sum
# n = int(input('Enter a numebr:'))
# m = int(input('Enter a numebr:'))

# result = add(n,m)  
# print(ressult)




# ___________________________Questions and Answers_________________________________#
# To find the below questions useing function

# qustion 1  Factorial 
# qustion 2 Fibannoci
# qustion 3 Palindrome
# qustion 4 Prime number
# qustion 5 Amstrong



# qustion 1  Factorial 

# def factorical(x):
    
#     n=1
#     for i in range(x):
#         n=n*x
#         x=x-1
#     return n
# x = int(input('Enter the number:'))
# result = factorical(x)
# print(result)

###################################################33

# qustion 2 Fibannoci


# def fibb(x):

#     a = 0
#     b = 1

#     if x==0:
#         print('fibnacci is:',x)
#     elif x>=1:
#         for i in range(x):

#             if x==1:
#                 print('fibnacci is:',x)
#             else:
#                 c=a+b
#                 a=b
#                 b=c
#                 print(c)
#     else:
#         print('wrong input',x)
        
# x = int(input('Enter a number:'))
# fibb(x)
###################################################################


# qustion 3 Palindrome

# def palin(x):
    
#     if x[::]==x[::-1]:
#         print('Palindrome')
#     else: 
#         print('Not Palindrome')
# x = str(input('Enter a number or string:'))
# palin(x)
#####################################################################



# qustion 4 Prime number

# def prime(x):

#     a = 0
#     if x==0 or x==1:
#         print('not prime')
#     else:
#         i=2
#         while i<x:
#             if x%i==0:
#                 a = a+1
#                 break
#             i = i+1
#     if a==0:
#         print('Prime')
#     else:
#         print('Not prime')

# x = int(input('Enter a number:'))
# prime(x)
#####################################################################


# qustion 5 Amstrong

# def amstrong(x):
    
#     k= 0

#     for i in x:
#         a=int(i)
#         a = a**len(x)
#         k=k+a

#     k=str(k)
#     k = list(k)
#     if k==x:
#         print('This is an Amstrong number')
#     else:
#         print('This is not an Amstrong number')

# x = list(input('Enter a number:'))
# amstrong(x)
#####################################################################