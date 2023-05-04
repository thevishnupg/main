import re

# x = 'sat mat cat rat bat '

# txt = re.findall(r'[smr]at',x)
# print(txt)     #this will print sat, mat and rat.

# txt = re.findall(r'[^smr]at',x)
# print(txt)   
# #this will print cat and bat. that is '^' this symbol is inveted the execution from 
# #the first print statement

##################################################################################

# Question 1 find words with the occurence of charecter 'z'

# x = 'zabc azbc abc akgkz'

# txt = re.findall(r'\w*z\w*',x)
# print(txt)

##################################################################################

# Question 2  List one digit two digit three digit...

# x = '1 12 123 1234 12345'

# txt = re.findall(r'\d{1}\s\d{2}\s\d{3}\s\d{4}\s\d{5}',x)
# print(txt)

###################################################################################

# Question 3  Find 3 letter 4letter 5 letter words in a sentece

# x = 'To find all three letter four letter and five letter words in a sentence'
# y = x[::-1]


# txt1 = re.findall(r'\w{3,5}',x)


# txt2 = re.findall(r'\w{3,5}',y)
# txt2_rev=(txt2[::-1])

# k1=' '
# k2=' '

# for i in txt1:
   
#    k1 = k1+i
# #    print(k1)


# for i in txt2_rev:

#     d=(i[::-1])
    
#     k2 = k2+d
#     # print(k2)

# print(k1)
# print(k2)
    
##################################################################################

# Question 4  Password validation

# x = input('Enter your password:')

# txt1 = len(x)
# txt2 = re.search(r'[a-z]',x)
# txt3 = re.search(r'[A-Z]',x)
# txt4 = re.search(r'[0-9]',x)
# txt5 = re.search(r'\s',x)
# txt6 = re.search(r'[@#$%&_*]',x)


# if txt1>8:
#     print('Not valid, Password should not grater than 8 letter')
# if not txt2:
#     print('Not valid , Password should contain one lower case letter')
# if not txt3:
#     print('Not valid, Password should contain one capital letter ')
# if not txt4:
#     print('Not valid, Password should contain one digit')
# if txt5:
#     print('Not valid, Password should not contain white space')
# if not txt6:
#     print('Not valid, Password should contain special charecter')
# else:
#     print('Password obtained.')

####################################################################################


# Question 5  Email validation

# x = input('Enter the email:')

# txt = re.match(r'[a-z 0-9]+\@[a-z 0-9]+\.[a-z]{2,3}$',x)

# if txt:
#     print('Email obtain:',x)
    
# else:
#     print('Wrong email')


