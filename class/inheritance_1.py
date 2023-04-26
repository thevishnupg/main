"""deposit, withdraval , balance of a person using inhertance"""


class Bank:
    def __init__(self,name,acc,bal):
        self.name = name
        self.ac = acc
        self.balance = bal

    def dep(self):
        d = int(input('Enter how much do you want to deposit :'))
        print('you deposit {}rupees'.format(d))
        self.balance += d
        print('Your balance is : ',self.balance)
        

    def wit(self):
        w = int(input('How much do you want to widrow :'))
        print('you want to withdraw {}rupees'.format(w))

        if w <= self.balance:
            balan= self.balance-w
            print('Your balcne is {} :'.format(balan))
        else:
            print('low balance')
    
    def baln(self):
        balan= self.balance
        print('Your balcne is {} :'.format(balan))
        print('Thankyou')
        

l=[]


while True:
    choice= int(input('Enter your choice (1-creat acc, 2- deposit, 3- withdrawal, 4-show balance, 5- exit):'))
    if choice==1:

        Person1=input('Enter the name:')
        acc=int(input('Enter the acc.number:'))
        ba = int(input('Enter the balace:'))
        ob=Bank(Person1,acc,ba)
        l.append(ob)

    if choice==2:
        acc = int(input('Enter your acc.number:'))
        for i in l:
            if i.ac==acc:
                
                i.dep()
            elif i.ac!=acc:
                print('Invalid acc.no')
    if choice==3:
        acc = int(input('Enter your acc.number:'))
        for i in l:
            if i.ac==acc:
                
                i.wit()
            elif i.ac!=acc:
                print('Invalid acc.no')
                
    if choice==4:
        acc = int(input('Enter your acc.number:'))
        for i in l:
            if i.ac==acc:
                
                i.baln()
            elif i.ac!=acc:
                print('Invalid acc.no')

    if choice==5:
        exit()

##################################################################################################################

# class Bank:
#     def __init__(self,name,acc):
#         self.name = name
#         self.acc = acc
#         self.balance = 500     

#     def dep(self):
#         d = int(input('Enter how much do you want to deposit :'))
#         print('you deposit {}rupees'.format(d))
#         total = self.balance + d
#         print('Your balance is : ',total)

#     def wit(self):
#         w = int(input('How much do you want to widrow :'))
#         print('you want to withdraw {}rupees'.format(w))
#         balan= self.balance-w
#         print('Your balcne is {} :'.format(balan))
    
#     def baln(self):
#         balan= self.balance
#         print('Your balcne is {} :'.format(balan))
#         print('Thankyou')


# class Person1(Bank):
#     def details(self, name, acc):
#         super().__init__(name, acc)
#         return('Name:',self.name,'acc.no:',self.acc)

#     pass


# nam=[]


# per1 = Person1(name=input('Enter the name:'),acc=int(input('Enter the acc.number:')))
# def p1():
#     per1.dep()
#     per1.wit()
#     per1.baln()

# p1()

