"""deposit, withdraval , balance of a person using inhertance"""


# class Bank:
#     def __init__(self,name,acc,bal):
#         self.name = name
#         self.ac = acc
#         self.balance = bal

#     def dep(self):
#         d = int(input('Enter how much do you want to deposit :'))
#         print('you deposit {}rupees'.format(d))
#         self.balance += d
#         print('Your balance is : ',self.balance)
        

#     def wit(self):
#         w = int(input('How much do you want to widrow :'))
#         print('you want to withdraw {}rupees'.format(w))

#         if w <= self.balance:
#             balan= self.balance-w
#             print('Your balcne is {} :'.format(balan))
#         else:
#             print('low balance')
    
#     def baln(self):
#         balan= self.balance
#         print('Your balcne is {} :'.format(balan))
#         print('Thankyou')
        

# l=[]


# while True:
#     choice= int(input('Enter your choice (1-creat acc, 2- deposit, 3- withdrawal, 4-show balance, 5- exit):'))
#     if choice==1:

#         Person1=input('Enter the name:')
#         acc=int(input('Enter the acc.number:'))
#         ba = int(input('Enter the balace:'))
#         ob=Bank(Person1,acc,ba)
#         l.append(ob)

#     if choice==2:
#         acc = int(input('Enter your acc.number:'))
#         for i in l:
#             if i.ac==acc:
                
#                 i.dep()
#             elif i.ac!=acc:
#                 print('Invalid acc.no')
#     if choice==3:
#         acc = int(input('Enter your acc.number:'))
#         for i in l:
#             if i.ac==acc:
                
#                 i.wit()
#             elif i.ac!=acc:
#                 print('Invalid acc.no')
                
#     if choice==4:
#         acc = int(input('Enter your acc.number:'))
#         for i in l:
#             if i.ac==acc:
                
#                 i.baln()
#             elif i.ac!=acc:
#                 print('Invalid acc.no')

#     if choice==5:
#         exit()

##################################################################################################################

# class Bank:
#     def __init__(self,name,acc):
#         self.name = name
#         self.acc = acc
#         self.balance = 500     

#     def dep(self):

#         d = int(input('Enter how much do you want to deposit :'))
#         print('you are deposit {}rupees'.format(d))
#         self.balance = self.balance+d
#         print('Your balance is : ',self.balance)

#     def wit(self):
#         w = int(input('How much do you want to widrow :'))
#         print('you have to withdraw {}rupees'.format(w))

#         if w <= self.balance:
#             self.balance = self.balance-w
#             print('Your balcne is {} :'.format(self.balance))
#         else:
#             print('low balance')
    
#     def bal(self):
#         balan= self.balance
#         print('Your current balcne is {} :'.format(balan))
#         print('Thankyou')

# class Person1(Bank):
#     def details(self,n,ac):
#         if n==self.name and ac==self.acc:
#             print()
#             print()
#             option= int(input('Select your option: 1 or 2 or 3 or 4 :'))  
#             print()  
#             if option==1:
#                 super().dep()
#                 print()
#                 opt= input('Want to do anything?: yes or no :')
#                 print()
#                 if opt=='yes' or 'Yes' or 'YES':
#                     per1.details(n=input('Type your name:'),ac=int(input('Type your ac.no:')))
#                 elif opt=='no' or 'No' or 'NO':
#                     exit()
#                 else:
#                     per1.details(n=input('Enter your name:'),ac=int(input('Enter your ac.no:')))

#             elif option==2:
#                 super().wit()
#                 print()
#                 opt= input('Want to do anything?: yes or no :')
#                 print()
#                 if opt=='yes' or 'Yes' or 'YES':
#                     per1.details(n=input('Type your name:'),ac=int(input('Type your ac.no:')))
#                 elif opt=='no' or 'No' or 'NO':
#                     exit()
#                 else:
#                     per1.details(n=input('Enter your name:'),ac=int(input('Enter your ac.no:')))

#             elif option==3:
#                 super().bal()
#                 print()
#                 opt= input('Want to do anything?: yes or no :')
#                 print()
#                 if opt=='yes' or 'Yes' or 'YES':
#                     per1.details(n=input('Type your name:'),ac=int(input('Type your ac.no:')))
#                 elif opt=='no' or 'No' or 'NO':
#                     exit()
#                 else:
#                     per1.details(n=input('Enter your name:'),ac=int(input('Enter your ac.no:')))
#             elif option==4:
#                 exit()
#             else:
#                 print('Incorrect input')
#                 print()
#                 per1.details(n=input('Enter your name:'),ac=int(input('Enter your ac.no:')))
#                 print()
#         else:
#             print()
#             print('Incorrect credintials')
#             print()

# per1 = Person1(name=input('Name:'),acc=int(input('Acc.Number:')))

# print()
# print()
# x = int(input('Enter 1 for further details and 2 for exit! :'))
# if x==1:
#     print()
#     print()
#     print('option 1:- deposit')
#     print('option 2:- withdrowel')
#     print('option 3:- balance')
#     print('option 4:- exit') 
#     print()
#     print()
#     per1.details(n=input('Enter your name:'),ac=int(input('Enter your ac.no:')))
#     print()
#     print()
# elif x==2:
#     print()
#     print('Thankyou')
#     print()
#     exit()
    
# else:
#     print('Your input is invalid!!!(type 1 or 2)')
