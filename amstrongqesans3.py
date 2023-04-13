# python program to check whether the number is amstrong or not

print()
print('Program to check whether the number is Amstrong or not')
print()

x = list(input('Enter a number:'))


k= 0

for i in x:
    a=int(i)
    a = a**len(x)
    k=k+a

k=str(k)
k = list(k)
if k==x:
    print('This is an Amstrong number')
else:
    print('This is not an Amstrong number')
