# Conditional statements are :- If ,else, elif ...

# question1: Find the larger number out of given 3 numbers

# a=1000
# b=670
# c=40

# if (a>b and a>c) :
#     print('a is large',a)
# elif (b>a and b>c) :
#     print('b is large',b)
# else:
#     print('c is large',c)



# question2:-  write down a program to check whether the entered number is divisible by 7 or not



# a = int(input('Enter a number :'))
# if (a%7==0):
#     print('Number is divisible by seven',a)
# else:
#     print('This number canot divisible by seven',a)



# question3:-  write down a program to check whether the entered number is even or odd



# a = int(input('Enter a number :'))
# if a%2==0:
#     print('Number is even',a)
# elif a%2 !=0:
#     print('Number is odd',a)
# else:
#     print('worng input',a)



# question4:-  write down a program to accept persantage of marks from user and print
# the grade



# a = int(input('Enter persantage of marks :'))

# if a>=90 and a<=100:
#     print('Grade A+',a)

# elif a>=80:
#     print('Grade A+',a)

# elif a>=70:
#     print('Grade B+',a)

# elif a>=60:
#     print('Grade B',a)

# elif a>=50:
#     print('Grade C+',a)

# elif a>=40:
#     print('Grade C',a)

# elif a>=30:
#     print('Grade D+',a)

# elif a>=20:
#     print('Grade D',a)

# else: 
#     print('Fail',a)



# question5:- write down a program to calculate the elctricity bill accept number from user according to the following criteria
# unit first 100 unit,  price no charge. next 100unit price 5 per/unit after 200 unit price 10 rs...

# x = int(input('Enter your electricity bill:'))
# charge=0

# if x<=100:
#     print('Amount',charge)
# elif x>100 and x<200:
#     charge=(x-100)*5
#     print('Amount',charge)
# elif x>200:
#     charge= ((x-200)*10)+(500)
#     print('Amount',charge)
# else:
#     print('dajfhaudhf')




#question6:- write down a programe to check the year is leap years or not 

# x=int(input('Enter the year:'))

# if x%400==0:
#     print('This is leap year',x)
# elif x%4==0:
#     print('This is a leap year')
# elif x%100==0:
#     print('This is leap year',x)
# else:
#     print('This is not leap year',x)


#question7:- write down the programe to check whether the number is positive or not

# x=int(input('Enter the number:'))

# if x<0:
#     print('Negative number')
# elif x>0:
#     print('Positive number')
# else:
#     print('wrong input')



#question8:- write down the programe to check 



# x=int(input('Enter Days (28,29,31,30):'))

# list_of_30=['March','June', 'Septamber', 'November' ]
# list_of_31=['January','April','May','July','August', 'October', 'December']
# list_of_28 =["February"]




# if x==31:
#     print('List of all 31 Days of Month:',list_of_31)
# elif x==30:
#     print('List of all 30 Days of Month:',list_of_30)
# elif x==28 or x==29:
#     print('List of all 28 or 29 Days of Month:',list_of_28)
# else:
#     print('worng input',x)


# y=(input('Enter The Month (first letter should be in capital):'))

# if y in list_of_30:
#     print(y,':- 30 days')
# elif y in list_of_31:
#     print(y,':- 31 days')
# elif y in list_of_28:
#     print(y,':- 28 or 29 days')
# else:
#     print('wrong input')
