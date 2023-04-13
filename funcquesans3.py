#Question 1 String patterns using function


# def pyt(x):

#     for i in range(len(x)):
#         for j in range(i+1):

#             print(x[j],end=' ')

#         print()

# pyt(input('Enter your string : '))
###########################################################


#Question 2 To calculate the count of elemnt presant in a string using function


# def count(x):
#     a={}
#     for i in x:
#         if i in a:
#             a[i]= a[i]+1
#         else:
#             a[i]=1
#     print(a)
# count(input('Enter a string:'))
##############################################################



#Question 3 Calculater using function
  


# def calculater(x,y):
#     print()
#     print()
#     print('option 1:- Addition')
#     print('option 2:- Substraction')
#     print('option 3:- Multiplication')
#     print('option 4:- Division')  
#     print()
#     print()
#     option= int(input('Select your option: 1 or 2 or 3 or 4 : '))
#     print()

#     if option==1:

#         def add():
#             z = x+y
#             print('Your answer is : ',z)
#         add()


#     elif option==2:

#         def subs():
#             z = x-y
#             print('Your answer is : ',z)
#         subs()

#     elif option==3:

#         def mult():
#             z = x*y
#             print('Your answer is : ',z)
#         mult()

#     elif option==4:

#         def divi():
#             z = x/y
#             print('Your answer is : ',z)
#         divi()

#     else:
#         print('something went wrong')
#         print('Thankyou')
        
#     return x,y
    


# calculater(float(input("Enter first number : ")),float(input("Enter second number : ")))

# ________________________________________________________ or _____________________________________________________________________

# def calculater(x,y):
#     print()
#     print()
#     print('option 1:- Addition')
#     print('option 2:- Substraction')
#     print('option 3:- Multiplication')
#     print('option 4:- Division')  
#     print('option 5:- EXIT') 
#     print()
#     print()
#     option= int(input('Select your option: 1 or 2 or 3 or 4 or 5 : '))
#     print()

#     if option==1:

#         def add():
#             z = x+y
#             print('Your answer is : ',z)
#         add()
#         print()
#         print("Do you want to calculate again? ")
#         user=int(input('press 6 for continue calcution: '))
#         if user==6:

#             calculater(float(input("Enter first number : ")),float(input("Enter second number : ")))
#         else:
#             exit()
#         print()

#     elif option==2:

#         def subs():
#             z = x-y
#             print('Your answer is : ',z)
#         subs()
#         print()
#         print("Do you want to calculate again? ")
#         user=int(input('press 6 for continue calcution: '))
#         if user==6:

#             calculater(float(input("Enter first number : ")),float(input("Enter second number : ")))
#         else:
#             exit()
#         print()

#     elif option==3:

#         def mult():
#             z = x*y
#             print('Your answer is : ',z)
#         mult()
#         print()
#         print("Do you want to calculate again? ")
#         user=int(input('press 6 for continue calcution: '))
#         if user==6:

#             calculater(float(input("Enter first number : ")),float(input("Enter second number : ")))
#         else:
#             exit()
#         print()
#     elif option==4:

#         def divi():
#             z = x/y
#             print('Your answer is : ',z)
#         divi()
#         print()
#         print("Do you want to calculate again? press number 6")
#         user=int(input('press 6 for continue calcution: '))
#         if user==6:

#             calculater(float(input("Enter first number : ")),float(input("Enter second number : ")))
#         else:
#             exit()
#         print()
#     elif option==5:
#         exit()

#     else:
#         print('something went wrong')
#         print('Thankyou')
        
#     return x,y
    


# calculater(float(input("Enter first number : ")),float(input("Enter second number : ")))

#########################################################################################################################



# Question 4 to print primenumber using function


# def prime(x):
#     for i in range (1,x+1):  
#         if i > 1:  
#             for j in range (2, i):  
#                 if (i % j) == 0:  
#                     break  
#             else:  
#                 print ( i, end=',')  
# prime(int(input('Enter a range:')))



# Question 5 to print reverse of a entered number without using reverse funciton

# def rev(x):
#     x=str(x)
#     return x[::-1]


# result = rev(int(input('Enter the number: ')))
# print(result)
###################################################################################

# Question 6 to print the sum of an entered number without using reverse funciton

# def sum(x):
#     a = 0
#     for i in x:
#         i = int(i)
#         a= a+i
        
#     print(a)

# sum(list(input('Enter the number: ')))
##########################################################################################


# Question 7 to print the vowels from a string and count the number of vowels presant in string


# def count(x):
#     a={}
#     for i in x:
#         if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#             if i in a:
#                 a[i]= a[i]+1
#             else:
#                 a[i]=1
#     print('Count of each vowels: ',a)
#     q = list(a.values())
#     k=0
#     for i in q:
#         k=k+i
#     print("Total number of vowels are:",k)


# count(input('Enter a string:'))
###################################################################################


# x = ['apple','grape','mango','banana']
# for i in x:
#     k=[]
#     a = [i]
#     print(a)
#     for i in a:
#         print([i])
        # if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        #     k.append(i)
        # print(k)

x = ['apple','grape','mango','banana']

for i in x:
    k=[]
    c=''
    for j in i:
        print(j,end='')
        if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u' or j=='A' or j=='E' or j=='I' or j=='O' or j=='U'):
            c=j
            k.append(c)

            print(k)
            # k.append(j)
            # print(j,end=',')
    print()
            

    




# def count(x):
#     a={}
#     for i in x:
#         if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
#             if i in a:
#                 a[i]= a[i]+1
#             else:
#                 a[i]=1
#     print('Count of each vowels: ',a)
#     q = list(a.values())
#     k=0
#     for i in q:
#         k=k+i
#     print("Total number of vowels are:",k)


# count(input('Enter the string:'))

# def vow(x):
#     for i in x:
#         if i in "aeiouAEIOU":
#             print(i, end=', ')

# x = input('Enter the string: ')
# vow(x)
# if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u' or a=='A' or a=='E' or a=='I' or a=='O' or a=='U'):