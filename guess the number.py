import random

from time import sleep

print(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

num = random.randint(1,15)

userinput=int(input('enter the number: '))

if userinput>15:
    print('number crosses the limit')
if userinput>num:
    print('number is smaller than', userinput)
if userinput<num:
    print('number is larger than', userinput)
if userinput == num:
    print('that is the correct number')

sleep(1)

print('the number is: ',num)
