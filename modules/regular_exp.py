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

x = input('Enter your password:')
txt = re.findall(r'\d*[a-z A-Z 0-9]',x)


if len(txt)<8:
    print('Password: ',txt)
else:
    print('Password must lower than 8 character')

####################################################################################


# Question 5  Email validation

# x = input('Enter the email:')

# txt = re.match(r'[a-z 0-9]+\@[a-z 0-9]+\.[a-z]{2,3}$',x)

# if txt:
#     print('Email obtain:',x)
    
# else:
#     print('Wrong email')



