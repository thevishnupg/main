# question1: write down the program to find number which is divisible by 5 and 7 between 1500 to 2700


# for i in range(1500,2701):
#     if i%5==0 and i%7==0:

#         print('The number',i,'is divisible by 5 and 7')
#     else:
#         print('The number',i,'is not divisible by 5 and 7')



# question2: write down the program to list with unique list


# x= [1,1,2,3,4,2]

# y = set(x)
# print(list(y))



# question2: write down the program to check whether the charecter is persent in user entered string


# x= input('Enter a string:')

# y= input('Enter an element:')

# if y in x:
#     print('The entered element', y ,'is presant in the string:')
# else:
#     print('The entered element', y ,'is not presant in the string:')




# question3: write down the program to print all even number that fall between two numbers entered from the user


# x= int(input('Enter a number:'))

# y= int(input('Enter another number:'))

# for i in range(x,(y+1)):
#     if i%2==0:
#         print(i)



# question4: write down the program to display only charecter which are presant at even index number


# x= (input('Enter a string:'))

# print(x[::2])


# question5: given two list , create new list;one contain odd numbers from first list and even numbers from second list




# x= [1,2,3,4,5,6,7,8,9,10]

# y= [11,3,64,9,2,7,12,21,22,23]
# a=[]

# for i in range(10):
    
#     if x[i]%2!=0:
        
#         a.append(x[i])
#     if y[i]%2==0:
#         a.append(y[i])
# a.sort()
# print(a)



# question6: print the squre of the number in a list


# x=[2,5,7,4,9,6,1]

# for i in x:
#     i=i**2
#     print(i)




# question5: print the series using for loop 
# 1: (10,20,30,40,50....)
# 2: (100,95,90,85,80....)



# for i in range(10):
#     i = i*10
#     print(i)

# for i in range(100,0,-5):
    
#     print(i)



